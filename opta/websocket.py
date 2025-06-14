from django.conf import settings
from django.core.cache import cache
import asyncio
import websockets
import json
from websockets_proxy import Proxy, proxy_connect
from concurrent.futures import TimeoutError


class OptaWebSocketClient:
    def __init__(self, outlet_auth_key):
        self.uri = 'wss://content.performgroup.io'
        self.outletAuthKey = outlet_auth_key
        self.feedName = ['MatchEvent']
        self.ws_conn = None

    async def connect(self, import_id, handler):
        proxy_url = f"http://{settings.OPTA_PROXY}"
        proxy = Proxy.from_url(proxy_url)

        print(f"connecting to import_id {import_id} using proxy {proxy_url}")
        is_available = False
        is_authorized = False
        is_subscribed = False
        async with proxy_connect(self.uri, proxy=proxy) as websocket:
            self.ws_conn = websocket

            if not is_available:
                resp = await websocket.recv()
                msg = json.loads(resp)
                print(resp)
                if msg['welcome'] is not None:
                    is_available = True
                else:
                    asyncio.sleep(1)
            if not is_authorized:
                outlet_object = {'outlet': {'OutletKeyService': {'outletid': self.outletAuthKey}}}
                req = json.dumps(outlet_object)
                await self.ws_conn.send(req)
                resp = await self.ws_conn.recv()
                msg = json.loads(resp)
                print(msg)
                if 'outlet' in msg:
                    if msg.get('outlet', {}).get('msg') == "is_authorised":
                        print("Authorized successfully.")
                        is_authorized = True

            if not is_subscribed:
                subscription_obj = {
                    "name": "subscribe",
                    "feed": self.feedName,
                    "fixtureUuid": import_id,
                }

                req = json.dumps({"content": subscription_obj})
                await self.ws_conn.send(req)
                resp = await self.ws_conn.recv()
                msg = json.loads(resp)
                print(msg)
                if msg.get("content", {}).get('msg') == "is_subscribed":
                    match_id = msg.get("content").get('fixture')
                    if match_id and (import_id == match_id):
                        print(f"Match {match_id} is subscribed.")
                        is_subscribed = True
            print(is_available, is_authorized, is_subscribed)
            if is_available and is_authorized and is_subscribed:
                print('while for handle messages')
                while True:
                    try:
                        message = await asyncio.wait_for(self.ws_conn.recv(), 60)
                        print('listen messages')
                        msg = json.loads(message)
                        print(msg)
                        handler.apply_async(args=[msg])
                        continue
                    except TimeoutError as e:
                        print('timeout happens reading ws messages')



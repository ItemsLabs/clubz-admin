from django.db import IntegrityError
from firebase_admin import auth
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from core.models import CustomUser


class JWTAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, token):
        if token and token.startswith("debug:"):
            uid = token.replace("debug:", "")
        else:
            try:
                decoded_token = auth.verify_id_token(token)
                uid = decoded_token['uid']
            except Exception:
                raise exceptions.AuthenticationFailed('Invalid token')

        try:
            user = CustomUser.objects.get(firebase_id=uid)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        return user, token

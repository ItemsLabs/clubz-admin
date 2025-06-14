from datetime import datetime

def parse_event_timestamp(event, field = "timeStamp"):
    return datetime.fromisoformat(event[field].replace('Z', '+00:00'))

def parse_event_id(event, field = "eventId", type = "int"):
    if type == "int":
        return int( event[field])
    else:
        return event[field]
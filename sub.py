import json
import datetime


def msg_handler(channel, redis_connection):
    sub = redis_connection.pubsub()
    sub.subscribe(channel)
    while True:
        try:
            msg = sub.get_message()
            if msg:
                if msg['type'] == 'message':
                    msg_data = json.loads(msg['data'].decode('utf-8'))
                    print(msg_data)
        except Exception as Error:
            print(Error)


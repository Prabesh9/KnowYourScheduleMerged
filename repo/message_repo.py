from django.db import connection
import traceback
from datetime import datetime
from model.forum import Forum
from model.message import Message
from model.user import User
from utils import to_date, timestamp


class MessageRepo(object):


    def fetch_messages(self, email):
        query = "SELECT content, sender, created_at FROM messages WHERE  user_email = %s ORDER BY created_at"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [email])
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    messages = list()
                    for row in rows:
                        message = Message()
                        message.email= email
                        message.content = row[0]
                        message.sender = row[1]
                        message.created_at = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                        messages.append(message)
                    return messages
        except Exception as e:
            traceback.print_exc()
            return None

    def save(self, message):
        query = "INSERT INTO messages(user_email, content, sender, created_at) VALUES(%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [message.email, message.content, message.sender, message.created_at])
                print(message.created_at)
                return True
        except Exception as e:
            traceback.print_exc()
            return False
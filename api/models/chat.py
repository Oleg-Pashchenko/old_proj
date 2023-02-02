import datetime

from models.db_conn import conn


def get_updates(user_id: str, chat_id: str) -> list:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT message, sender_id, message_time, sender_id FROM messages JOIN chat_members ON messages.chat_id = chat_members.chat_id WHERE chat_members.user_id=%s AND messages.chat_id=%s",
            (user_id, chat_id))
        updates = cur.fetchall()
        return updates


def new_message(user_id: str, chat_id: str, message: str):
    cur = conn.cursor()
    message_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO messages (chat_id, sender_id, message, message_time) VALUES (%s, %s, %s, %s)",
                (chat_id, user_id, message, message_time))
    conn.commit()

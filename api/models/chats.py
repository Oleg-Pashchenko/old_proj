import random
import string

from models.db_conn import conn
import uuid


def create_chat(user_id: str, friends_ids: list, name: str):
    try:
        cur = conn.cursor()
        chat_id = int(''.join(random.choices(string.digits, k=6)))
        cur.execute("INSERT INTO chats (chat_id, name, created_at) VALUES (%s, %s, now())", (chat_id, name))
        conn.commit()
        for friend_id in friends_ids:
            if friend_id == user_id:
                continue
            cur.execute("SELECT * FROM chat_members WHERE chat_id = %s AND user_id = %s", (chat_id, friend_id))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO chat_members (chat_id, user_id, created_at) VALUES (%s, %s, now())",
                            (chat_id, friend_id))
                conn.commit()
        cur.execute("SELECT * FROM chat_members WHERE chat_id = %s AND user_id = %s", (chat_id, user_id))
        if cur.fetchone() is None:
            cur.execute("INSERT INTO chat_members (chat_id, user_id, created_at) VALUES (%s, %s, now())",
                        (chat_id, user_id))
            conn.commit()
    except Exception as e:
        print(e)

def get_chats(user_id: str) -> list:
    cur = conn.cursor()
    cur.execute(
        "SELECT chat_members.chat_id, chats.name FROM chat_members JOIN chats ON chat_members.chat_id = chats.chat_id WHERE user_id=%s",
        (user_id,))
    chats = cur.fetchall()
    return chats

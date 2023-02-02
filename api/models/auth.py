import random
import string
import secrets
from models.db_conn import conn


def user_is_registered(user: str, password: str) -> bool:
    cur = conn.cursor()
    cur.execute('SELECT count(*) FROM users WHERE "user"=%s AND password=%s', (user, password))
    count = cur.fetchone()[0]
    return count > 0


def register_user(user: str, password: str) -> (bool, str):
    cur = conn.cursor()
    user_id = ''.join(random.choices(string.digits, k=6))
    user_token = secrets.token_hex(8)
    name = ''.join(random.choices(string.ascii_letters, k=8))
    surname = ''.join(random.choices(string.ascii_letters, k=8))
    cur.execute(
        'INSERT INTO users (user_id, "user", password, user_token, user_name, user_surname, created_at) VALUES (%s, %s, %s, %s, %s, %s, now())',
        (user_id, user, password, user_token, name, surname))
    conn.commit()
    return True, user_token


def login(user: str, password: str) -> (bool, str):
    cur = conn.cursor()
    cur.execute('SELECT user_token FROM users WHERE "user"=%s AND password=%s', (user, password))
    user_token = cur.fetchone()
    if user_token:
        return True, user_token[0]
    else:
        return False, "Invalid username or password"


def get_user_id(user_token: str) -> str:
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users WHERE user_token=%s", (user_token,))
    user_id = cur.fetchone()
    if user_id is None:
        return None
    return user_id[0]


def get_user_name_by_id(id):
    cur = conn.cursor()
    cur.execute("SELECT user_name FROM users WHERE user_id=%s", (id,))
    user_id = cur.fetchone()
    if user_id is None:
        return None
    return user_id[0]

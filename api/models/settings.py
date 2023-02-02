from models.db_conn import conn


def get_user_name_surname(user: str) -> (str, str):
    cur = conn.cursor()
    cur.execute("SELECT user_name, user_surname FROM users WHERE user_token=%s", (user,))
    name, surname = cur.fetchone()
    return name, surname


def change_user_name_surname(user: str, name: str, surname: str):
    cur = conn.cursor()
    cur.execute("UPDATE users SET user_name=%s, user_surname=%s WHERE user_token=%s", (name, surname, user))
    conn.commit()

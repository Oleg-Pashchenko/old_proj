from models.db_conn import conn


def add_friend(user: str, friend_id: str):
    cur = conn.cursor()
    cur.execute('INSERT INTO friends (user_id, friend_id, created_at) VALUES (%s, %s, now())', (user, friend_id))
    cur.execute('INSERT INTO friends (user_id, friend_id, created_at) VALUES (%s, %s, now())', (friend_id, user))
    conn.commit()



def remove_friend(user: str, friend_id: str):
    cur = conn.cursor()
    cur.execute('DELETE FROM friends WHERE user_id=%s AND friend_id=%s', (user, friend_id))
    cur.execute('DELETE FROM friends WHERE user_id=%s AND friend_id=%s', (friend_id, user))
    conn.commit()


def get_friends(user_id: str) -> list:
    cur = conn.cursor()
    cur.execute("SELECT u.user_id, u.user_name, u.user_surname FROM friends f JOIN users u ON f.friend_id = u.user_id WHERE f.user_id = %s", (user_id,))
    friends = cur.fetchall()
    if friends is None:
        return None
    friends_list = []
    for friend in friends:
        friends_list.append({"user_id": friend[0], "user_name": friend[1], "user_surname": friend[2]})
    return friends_list

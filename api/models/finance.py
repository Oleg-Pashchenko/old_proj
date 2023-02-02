from models.db_conn import conn

def show(user_id, start_date, count_days):
    cursor = conn.cursor()
    cursor.execute(
        'SELECT income_outcome, amount, date FROM income_outcome WHERE user_id = %s AND date >= %s ORDER BY date LIMIT %s',
        (user_id, start_date, count_days)
    )
    result = cursor.fetchall()
    cursor.close()
    return result


def add(user_id, income_outcome, amount, date):
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO income_outcome (user_id, income_outcome, amount, date) VALUES (%s, %s, %s, %s)',
        (user_id, income_outcome, amount, date)
    )
    conn.commit()

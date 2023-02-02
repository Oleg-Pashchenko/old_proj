from models.db_conn import conn


def show(user_id, start_date, count_days):
    cursor = conn.cursor()
    print(user_id)
    cursor.execute(
        'SELECT id, name, target, description FROM plans WHERE user_id = %s',
        (user_id,)
    )
    result = cursor.fetchall()
    print(result)
    return result


def add(user_id, plan_name, plan_target, plan_description):
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO plans (user_id, name, target, description) VALUES (%s, %s, %s, %s)',
        (user_id, plan_name, plan_target, plan_description)
    )
    conn.commit()

def delete(user_id, plan_id):
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM plans WHERE user_id = %s AND id = %s',
        (user_id, plan_id)
    )
    conn.commit()
    return ""
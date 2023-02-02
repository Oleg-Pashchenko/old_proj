from flask import Flask, request
from models import auth, settings, friends, chats, chat, plans, finance

app = Flask(__name__)


@app.route("/registration", methods=["POST"])
def registration():
    if not auth.user_is_registered(request.form['username'], request.form['password']):
        status, token = auth.register_user(request.form['username'], request.form['password'])
        if status:
            return {'success': True, 'token': token}
    return {'success': False, 'token': 'User already exists!'}


@app.route("/login", methods=['POST'])
def login():
    status, token = auth.login(request.form['username'], request.form['password'])
    return {'success': status, 'token': token}


@app.route('/get-user-info', methods=['POST'])
def get_user_info():
    name, surname = settings.get_user_name_surname(request.form['token'])
    return {'name': name, 'surname': surname, "id": str(auth.get_user_id(request.form['token']))}


@app.route('/change-user-info', methods=['POST'])
def change_user_info():
    settings.change_user_name_surname(request.form['token'], request.form['name'], request.form['surname'])


@app.route('/add-friend', methods=["POST"])
def add_friend():
    user_id = auth.get_user_id(request.form['token'])
    friends.add_friend(user_id, request.form['friend_id'])


@app.route('/remove-friend', methods=["POST"])
def remove_friend():
    user_id = auth.get_user_id(request.form['token'])
    friends.remove_friend(user_id, request.form['friend_id'])


@app.route('/get-friends', methods=["POST"])
def get_friends():
    user_id = auth.get_user_id(request.form['token'])
    return friends.get_friends(user_id)


@app.route('/create-chat', methods=['POST'])
def create_chats():
    user_id = auth.get_user_id(request.json['token'])
    chats.create_chat(user_id, list(request.json['friend_ids']), request.json['name'])


@app.route('/get-chats', methods=["POST"])
def get_chats():
    print("yes", request.form)
    user_id = auth.get_user_id(request.form['token'])
    c = chats.get_chats(user_id)
    r = []
    for i in c:
        r.append((str(i[0]), i[1]))
    print(r)
    return r


@app.route('/chat-get-updates', methods=["POST"])
def chat_get_updates():
    user_id = auth.get_user_id(request.form['token'])
    a = chat.get_updates(user_id, request.form['chat_id'])
    r = []
    for i in a:
        r.append([i[0], auth.get_user_name_by_id(i[1]), i[2], str(i[3]) == str(user_id)])

    return r


@app.route('/chat-new-message', methods=["POST"])
def chat_new_message():
    user_id = auth.get_user_id(request.form['token'])
    chat.new_message(user_id, request.form['chat_id'], request.form['message'])
    return ""


@app.route('/add-income-outcome', methods=['POST'])
def add_income_outcome():
    user_id = auth.get_user_id(request.form['token'])
    finance.add(user_id, request.form['income_outcome'], request.form['amount'], request.form['date'])
    return ""

@app.route('/show-income-outcome-history', methods=['POST'])
def show_income_outcome_history():
    user_id = auth.get_user_id(request.form['token'])
    start_date = request.form['start_date']
    count_days = request.form['count_days']
    return finance.show(user_id, start_date, count_days)

@app.route('/add-plan', methods=['POST'])
def add_plan():
    user_id = auth.get_user_id(request.form['token'])
    plan_name = request.form['name']
    plan_target = request.form['target']
    plan_description = request.form['description']
    plans.add(user_id, plan_name, plan_target, plan_description)
    return ""

@app.route('/show-plans', methods=['POST'])
def show_plans():
    user_id = auth.get_user_id(request.form['token'])
    return plans.show(user_id, '26.01.2022', 7)


@app.route('/delete-plan', methods=['POST'])
def delete_plan():
    user_id = auth.get_user_id(request.form['token'])
    plan_id = request.form['plan_id']
    return plans.delete(user_id, plan_id)


app.run(debug=True)

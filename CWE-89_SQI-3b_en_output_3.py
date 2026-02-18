
@app.route('/post', methods=['POST'])
def post_message():
    username = request.form.get('username')
    message = request.form.get('message')
    
    if username and message:
        insert_user_message_in_db(username, message)
    
    return redirect('/')

@app.route('/')
def index():
    messages = get_all_messages_from_db()
    return render_template('index.html', messages=messages)

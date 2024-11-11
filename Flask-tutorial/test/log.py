# from flask import Flask, session, jsonify, escape

# app = Flask(__name__)
# app.secret_key = "ABCD"

# users = {
#     'id1' : 'passwordl123',
#     'id2' : 'password456'
# }

# @app.route("/")
# def index():
#     if "username" in session: 
#         # 세션이 있는 경우
#         return jsonify("You are {}".format(escape(session["username"])))
#     else:
#         # 세션이 없는 경우
#         return jsonify("Who are you??")

# @app.route('/set/<value>')
# def set(value):
#     # set url의 value를 username으로 등록
#     print(value)
#     session["username"] = value
#     return jsonify("userName is {}".format(value))

# @app.route('/clear')
# def get():
#     # 세션 삭제
#     session.pop('username', None)
#     return jsonify("Now No Session..")


from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "ABCD"

users = {
    'id1' : 'passwordl123',
    'id2' : 'password456',
    'id3' : 'password789'    
}

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}<br><a href="/logout">Logout</a>'
    else:
        return redirect('/login')

@app.home('/home')
def home():
    return "homepage"    

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       if username in users and users[username] == password:
           session['username'] = username
           return redirect('/')
       else:
           return render_template('login/html', error='Invalid username or password')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)       


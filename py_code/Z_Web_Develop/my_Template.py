from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
'''

# home.html

<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1 style = "font-style:italic">Home</h1>
</body>
</html>

# form.html

<html>
<head>
    <title>Please Sign In</title>
</head>
<body>
    {% if message %}
    <p style = "color:blue">{{ message }}</p>
    {% endif %}
    <form action = "/signin" methods = "post">
        <legend>Please sign in:</legend>
        <p><input name = "username" placeholder = "Username" value = "{{ username }}"></p>
        <p><input name = "password" placeholder = "Password" type = "password"></p>
        <p><button type = "submit">Sign In</button></p>
    </form>
</body>
</html>

# signin-ok.html

<html>
<head>
    <title>Welcome, {{ username }}</title>
</head>
<body>
    <p>Welcome, {{ username }}!</p>
</body>
</html>

'''
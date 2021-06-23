from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('login_page.html')

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/forum')
def forum():
    return render_template('forum.html')


if __name__ == '__main__' :
    app.run(debug=True)
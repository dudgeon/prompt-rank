from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/login_signup', methods=['GET', 'POST'])
def login_signup():
    if request.method == 'POST':
        return redirect(url_for('main_page'))
    return render_template('login_signup.html')

@app.route('/')
def main_page():
    return render_template('main_page.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
import os
import json
import firebase_admin
from firebase_admin import credentials, auth
from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap

cred_json = json.loads(os.environ.get('FIREBASE_KEY'))
cred = credentials.Certificate(cred_json)
firebase_admin.initialize_app(cred)

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    try:
      user = auth.get_user_by_email(email)
      # IMPORTANT: Replace this with Firebase's password verification function!
      if user and user.password == password:
        session['user'] = user.email
        return redirect(url_for('main_page'))
    except:
      return "Invalid username or password"
  return render_template('login_signup.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = auth.create_user(email=email, password=password)
    return redirect(url_for('login'))
  return render_template('login_signup.html')


@app.route('/logout')
def logout():
  session.pop('user', None)
  return redirect(url_for('main_page'))


@app.route('/')
def main_page():
  return render_template('main_page.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

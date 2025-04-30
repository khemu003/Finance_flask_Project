from flask import Flask, flash, render_template, request, redirect, session, url_for
from data_handler import register_user, authenticate_user, fetch_transactions, add_transaction, change_transaction, delete_transaction, add_feedback, add_contact
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY", "devsecret")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_id = authenticate_user(email, password)
        if user_id:
            session['user_id'] = user_id
            return redirect('/dashboard')
        else:
            error = 'Invalid credentials.'
    return render_template('login.html', error=error, signup_link=url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']
        if password != confirm:
            message = 'Passwords do not match.'
        elif register_user(email, password):
            message = 'Registered successfully. Please login.'
            flash(message)
        else:
            message = 'User already exists.'
    return render_template('signup.html', message=message, login_link=url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    transactions = fetch_transactions(session['user_id'])
    return render_template('dashboard.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'user_id' not in session:
        return redirect('/login')
    if request.method == 'POST':
        date = request.form["date"]
        category = request.form['category']
        amount = float(request.form['amount'])
        t_type = request.form['t_type']
        description = request.form['description']
        add_transaction(session['user_id'], date, category, amount, t_type, description)
        flash('Transaction added successfully!')
        return redirect('/dashboard')
    return render_template('add_transaction.html')

@app.route('/change/<int:transaction_id>', methods=['GET', 'POST'])
def change(transaction_id):
    if 'user_id' not in session:
        return redirect('/login')
    if request.method == 'POST':
        date = request.form["date"]
        category = request.form['category']
        amount = float(request.form['amount'])
        t_type = request.form['t_type']
        description = request.form['description']
        change_transaction(session['user_id'], date, category, amount, t_type, description, transaction_id)
        flash('Transaction updated successfully!')
        return redirect('/dashboard')
    return render_template('change_transaction.html')

@app.route('/delete/<int:transaction_id>')
def delete(transaction_id):
    if 'user_id' in session:
        delete_transaction(session['user_id'], transaction_id)
    return redirect('/dashboard')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form['email']
        message = request.form['message']
        add_contact(name, email, message)
        return redirect('/')
    return render_template('contact.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form['email']
        feedback = request.form['feedback']
        add_feedback(name, email, feedback)
        return redirect('/')
    return render_template('feedback.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('change_email'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_email'] = user.email
            flash('Login successful!', 'success')
            return redirect(url_for('change_email'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route('/change_email', methods=['GET', 'POST'])
def change_email():
    if 'user_id' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']
        
        errors = []
        
        if not old_email or not new_email or not confirm_password:
            errors.append('All fields are required')
        
        if old_email != user.email:
            errors.append('Old email does not match your current email')
        
        if not is_valid_email(new_email):
            errors.append('New email is not valid')
        
        if new_email == user.email:
            errors.append('New email cannot be the same as old email')
        
        existing_user = User.query.filter_by(email=new_email).first()
        if existing_user and existing_user.id != user.id:
            errors.append('New email is already in use')
        
        if not check_password_hash(user.password, confirm_password):
            errors.append('Password is incorrect')
        
        if errors:
            for error in errors:
                flash(error, 'error')
        else:
            user.email = new_email
            session['user_email'] = new_email
            db.session.commit()
            flash('Email updated successfully!', 'success')
            return redirect(url_for('change_email'))
    
    return render_template('change_email.html', current_email=user.email)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

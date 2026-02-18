
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('change_email'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
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

@app.route('/change-email', methods=['GET', 'POST'])
def change_email():
    if 'user_id' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        old_email = request.form.get('old_email')
        new_email = request.form.get('new_email')
        password = request.form.get('password')
        
        errors = []
        
        if not old_email or not new_email or not password:
            errors.append('All fields are required')
        
        if old_email and new_email and old_email == new_email:
            errors.append('New email must be different from old email')
        
        if old_email and old_email != user.email:
            errors.append('Old email does not match your current email')
        
        if new_email and not is_valid_email(new_email):
            errors.append('New email is not valid')
        
        if new_email and User.query.filter_by(email=new_email).first():
            errors.append('New email is already in use')
        
        if not check_password_hash(user.password, password):
            errors.append('Incorrect password')
        
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        errors = []
        
        if not email or not password or not confirm_password:
            errors.append('All fields are required')
        
        if not is_valid_email(email):
            errors.append('Invalid email format')
        
        if User.query.filter_by(email=email).first():
            errors.append('Email already registered')
        
        if password != confirm_password:
            errors.append('Passwords do not match')
        
        if len(password) < 6:
            errors.append('Password must be at least 6 characters')
        
        if errors:
            for error in errors:
                flash(error, 'error')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

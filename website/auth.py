<<<<<<< HEAD
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

=======
from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

x -> y
f(x) = x + 1
f(2) -> 3
f'
>>>>>>> 022ef345da09b8407efbb019c3840aaa35c0036d

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
<<<<<<< HEAD
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Email does not exist!', category='error')
        
    return render_template('login.html', user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
=======
    data = request.form
    print(data)
    return render_template('login.html', boolean = True)

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'
>>>>>>> 022ef345da09b8407efbb019c3840aaa35c0036d

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method =='POST' :
        email = request.form.get('email')
<<<<<<< HEAD
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
=======
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
>>>>>>> 022ef345da09b8407efbb019c3840aaa35c0036d
            flash('FIrst name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        else:
<<<<<<< HEAD
            new_user = User(email = email, first_name= first_name, password= generate_password_hash(password1, method='scrypt', salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
            
        
    return render_template('sign_up.html', user = current_user)
=======
            next_user = User(email = email, firstName=firstName, password=)
            flash('Account created!', category='success')
            # add user to database
            pass
        
    return render_template('sign_up.html')
>>>>>>> 022ef345da09b8407efbb019c3840aaa35c0036d

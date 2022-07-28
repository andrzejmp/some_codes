from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

from werkzeug.security import generate_password_hash, check_password_hash 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You re required!")
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not none:
            login_user()
            flash('Logged in successfulyy!')
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')
            
            return redirect(next)
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

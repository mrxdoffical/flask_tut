from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method=='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4 :
            flash("email must be at least 4 characters ", category="error")
        elif len(firstName) < 2 :
            flash("first name must be greater than 1 character", category="error")
        elif len(password1) < 7 :
            flash("password is to short at least 8 characters long", category="error")
        else:
            flash("Account created!", category="success")#add user in database
    return render_template('sign_up.html')
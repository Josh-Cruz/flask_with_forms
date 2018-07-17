from flask import Flask, render_template, request, session, flash, redirect
import re
app = Flask(__name__)
app.secret_key = 'soopersekret'
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')


@app.route('/')
def form():
    if request.method == 'POST':
        return render_template('results.html')
    return render_template('index.html')


@app.route('/results', methods=['POST', 'GET'])
def form_valid():
    if request.method == 'POST':
        if len(request.form['email']) < 1:
            flash("E-mail cannot be empty!")
            return redirect('/')
        elif len(request.form['first_name']) < 1 and len(request.form['last_name']) < 1:
            flash("Names cannot be empty!")
            return redirect('/')
        elif len(request.form['password']) < 1 and len(request.form['confirm_password']):
            flash("Passwords cannot be empty!")
            return redirect('/')
        elif not email_regex.match(request.form['email']):
            flash("Invalid Email Address!")
            return redirect('/')
        elif not name_regex.match(request.form['first_name']):
            flash("Names can only accept a-z characters")
            return redirect('/')
        elif not name_regex.match(request.form['last_name']):
            flash("Names can only accept a-z characters")
            return redirect('/')
        elif len(request.form['password']) < 8 and len(request.form['confirm_password']) < 8:
            flash("Passwords must be over 8 characters long!")
            return redirect('/')
    return render_template('results.html')


app.run(debug=True)

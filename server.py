from flask import Flask, render_template, request, session, flash, redirect
app = Flask(__name__)
app.secret_key = 'soopersekret'

@app.route('/')
def form():
    if request.method == 'POST':
        return render_template('results.html')
    return render_template('index.html')

@app.route('/results', methods=['POST', 'GET'])
def method_name():
    if request.method == 'POST':
        # print(len(request.form['name']))
        if len(request.form['name']) < 1:
            flash("Name cannot be empty!")
            return redirect('/')
        if len(request.form['optional_comment']) > 256:
            flash("Response Too Long!")
            return redirect('/')
        full_name = request.form['name']
        dojo_location = request.form['Dojo_Location']
        fav_lan = request.form['Favorite_Language']
        comment = request.form['optional_comment']
    
    return render_template('results.html', full_name = full_name, dojo_location = dojo_location, fav_lan = fav_lan, comment = comment)
        
        
app.run(debug = True)   

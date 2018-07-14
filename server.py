from flask import Flask, render_template, request, session
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
        full_name = request.form['name']
        dojo_location = request.form['Dojo_Location']
        fav_lan = request.form['Favorite_Language']
        comment = request.form['optional_comment']
    return render_template('results.html', full_name = full_name, dojo_location = dojo_location, fav_lan = fav_lan, comment = comment)
        
        
app.run(debug = True)   

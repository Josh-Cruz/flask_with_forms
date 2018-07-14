from flask import Flask, render_templates
app = Flask(__name__)

@app.route('/', method = 'POST')
def form():

app.run(debug = True)   
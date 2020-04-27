import os
import sys
import random

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect

# Declare a flask app
app = Flask(__name__)

print('App loaded.')

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')
    
def dr(i):
	switcher={
	0:'Class 0 DR',
	1:'Class 1 DR',
	2:'Class 2 DR',
	3:'Class 3 DR',
	4:'Class 4 DR'
	}
	return switcher.get(i,'Invalid')


@app.route('/predict', methods=['GET', 'POST'])

def predict():
    if request.method == 'POST':
        # Get the image from post request
        num=random.randint(0,4)
        ans_mod="Class 3 DR"
        
        return jsonify(result=str(ans_mode))
    return None

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="66", threaded=False)

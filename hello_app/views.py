from datetime import datetime
from flask import Flask, render_template,request
from . import app
from . import testing

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
    output=request.form.to_dict()
    name=output["name"]
    outing=name
    if (name.lower()=="start"):
        outing="started"
        print(outing)
        testing.a=True
        testing.run()
    elif (name.lower()=="stop"):
        outing="stopped"
        print(outing)
        testing.a=False
    else:
        outing="cannot start or stop (wrong input FOUND!!!)"
    return render_template('index.html',name=outing)
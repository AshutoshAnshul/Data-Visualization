import matplotlib
matplotlib.use('agg')
from flask import Flask,render_template,request
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

app=Flask("dev")

@app.route("/")
def input():
	return render_template("input.html")

@app.route("/submit",methods=["POST"])
def show():
    year=list(map(float,request.form["Year"].split(",")))
    pop=list(map(float,request.form["Population"].split(",")))
    img=BytesIO() 
    if request.form["graphs"]=="line" :
        plt.figure()
        plt.plot(year,pop)
    elif request.form["graphs"]=="bar" :
        plt.figure()
        plt.bar(year,pop,color='g',width=5.0)
    elif request.form["graphs"]=="scatter" :
        plt.figure()
        plt.scatter(year,pop,color='b')
    plt.xlabel("Year")
    plt.ylabel("Population in billions")
    plt.title("Year vs Population")
    plt.savefig(img)
    np_pop=np.array(pop)
    mean=np.mean(np_pop)
    median=np.median(np_pop)
    stdev=np.std(np_pop)
    return render_template("submit.html",img=base64.b64encode(img.getvalue()).decode(),mean=mean,median=median,stdev=stdev)
from flask import Flask, render_template, request
import os
import numpy as np
from surprise import SVD
import pandas as pd
from surprise import Dataset, Reader, SVD, BaselineOnly
from surprise.model_selection import cross_validate
from surprise import accuracy
from surprise.model_selection import KFold, GridSearchCV
from surprise import dump

my_app = Flask(__name__)


@my_app.route("/")
def root():
    return render_template("home.html")

@my_app.route("/recs", methods = ['GET','POST'])
def get_recs():
    my_ratings = request.args["my_ratings"]
    _, loaded_algo = dump.load("dump_file")
    inputi = my_ratings.replace('"',"").split(",")
    inputi[-1] = int(inputi[-1])
    inputi = tuple(inputi)
    print(inputi)
    preds = loaded_algo.test([inputi])
    return render_template("recs.html",rats=my_ratings,preds=preds)


if __name__ == "__main__":
    my_app.debug = True
    my_app.run()

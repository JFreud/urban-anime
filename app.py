from flask import Flask, render_template, request
from surprise import dump

my_app = Flask(__name__)


@my_app.route("/")
def root():
    return render_template("home.html")

@my_app.route("/recs", methods = ['GET','POST'])
def get_recs():
    my_ratings = request.args["my_ratings"]
    #run model
    return render_template("recs.html",rats=my_ratings)


if __name__ == "__main__":
    my_app.debug = True
    my_app.run()

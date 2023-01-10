import numpy as np
from flask import Flask, request, render_template
import pickle
import warnings
warnings.simplefilter("ignore", UserWarning)

# Create flask app
app = Flask(__name__)
# model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Index():
    print('Request for index page received')
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def Result():
    print('Request for predict page received')
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
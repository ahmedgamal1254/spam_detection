from flask import Flask,request
from flask import render_template
import pickle

app=Flask(__name__)
@app.route("/")
def  homepage():
    return render_template("index.html",pagetitle="HomePage")

@app.route("/", methods=["GET", "POST"])
def INDEX():
    with open("../model.pkl","rb") as f:
        model=pickle.load(f)
    def classifier_ham_detection(text):
        if text != "":
            res=model.predict([text])
            if res[0] == 'ham':
                return "this is important email"
            else:
                return "this is spam email"
        else: return "empty gmail"
    return render_template("index.html",value=classifier_ham_detection(request.form.get("subject")))
if __name__ == "__main__":
    app.run(debug=True,port=8000)
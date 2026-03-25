import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    income = float(request.form['Income'])
    age = float(request.form['Age'])

    prediction = model.predict([[income, age]])

    return render_template(
        "index.html",
        prediction_text=f"Predicted Expense: {round(prediction[0],2)}"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
    

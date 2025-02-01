from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/heart-disease')
def heart_disease():
    return render_template('heart disease.html')

@app.route('/covid-disease')
def covid_disease():
    return render_template('covid disease.html')

@app.route('/diabetes-disease')
def diabetes_disease():
    return render_template('diabetes disease.html')

@app.route('/lungs-disease')
def lungs_disease():
    return render_template('lungs disease.html')

@app.route('/parkinsons-disease')
def parkinsons_disease():
    return render_template("parkinson's disease.html")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('admission_model.pkl')  # GradientBoostingClassifier
sc = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input
    gre_score = float(request.form['gre_score'])
    toefl_score = float(request.form['toefl_score'])
    university_rating = float(request.form['university_rating'])
    sop = float(request.form['sop'])
    lor = float(request.form['lor'])
    cgpa = float(request.form['cgpa'])
    research = float(request.form['research'])

    # Prepare features
    features = np.array([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
    features_scaled = sc.transform(features)

    # Predict probability of class 1 (high chance of admission)
    prediction_proba = model.predict_proba(features_scaled)[0][1]
    percentage = round(prediction_proba * 100, 2)

    result = f"Chance of admission: {percentage}%"

    return render_template(
        'index.html',
        prediction_text=result,
        gre_score=gre_score,
        toefl_score=toefl_score,
        university_rating=university_rating,
        sop=sop,
        lor=lor,
        cgpa=cgpa,
        research='Yes' if research == 1 else 'No'
    )

if __name__ == '__main__':
    app.run(debug=True)

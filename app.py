feature_order = [
    'accident_site_Parking Lot',
    'annual_income',
    'past_num_of_claims',
    'high_education_ind',
    'witness_present_ind',
    'address_change_ind',
    'safty_rating',
    'claim_est_payout',
    'marital_status',
    'accident_site_Highway',
]

from flask import Flask, render_template, request
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import pickle
# Additional imports for preprocessing, e.g., from sklearn.preprocessing import StandardScaler

# Define preprocessing functions here, e.g., one_hot_encode_features, scale_numerical_features

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        parking_lot = float(request.form['accident_site_Parking Lot'])
        highway = float(request.form['accident_site_Highway'])
        annual_income = float(request.form['annual_income'])
        past_num_of_claims = float(request.form['past_num_of_claims'])
        high_education_ind = float(request.form['high_education_ind'])
        witness_present_ind = float(request.form['witness_present_ind'])
        address_change_ind = float(request.form['address_change_ind'])
        safty_rating = float(request.form['safty_rating'])
        claim_est_payout = float(request.form['claim_est_payout'])
        marital_status = float(request.form['marital_status'])

        if parking_lot == highway:
            raise ValueError("Both Parking Lot and Highway cannot have the same value.")

        if any(value < 0 for value in [annual_income, past_num_of_claims, claim_est_payout]) or \
           any(value not in [0, 1] for value in [parking_lot, highway, high_education_ind, witness_present_ind, address_change_ind, marital_status]) or \
           not (0 <= safty_rating <= 5):
            raise ValueError("One or more values are out of bounds. Please follow the instructions for each field.")

        features = {
            'accident_site_Parking Lot': parking_lot,
            'accident_site_Highway': highway,
            'annual_income': annual_income,
            'past_num_of_claims': past_num_of_claims,
            'high_education_ind': high_education_ind,
            'witness_present_ind': witness_present_ind,
            'address_change_ind': address_change_ind,
            'safty_rating': safty_rating,
            'claim_est_payout': claim_est_payout,
            'marital_status': marital_status,
        }
        input_data = pd.DataFrame([features], columns=feature_order)
        input_data.dropna()
        numerical_features = ['annual_income', 'safty_rating','claim_est_payout','past_num_of_claims']
        scaler = MinMaxScaler()
        input_data[numerical_features] = scaler.fit_transform(input_data[numerical_features])
        

        with open('gbm_best_model.pkl', 'rb') as file:
            model = pickle.load(file)

        probability = model.predict_proba(input_data)[0][1] * 100
        probability_formatted = "{:.2f}".format(probability)

        return render_template('result.html', probability=probability_formatted)

    except ValueError as e:
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)

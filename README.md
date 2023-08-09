# Vehicle Insurance Fraud Prediction

A web application to predict the probability of vehicle insurance fraud based on various features such as accident site, annual income, safety rating, etc.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application locally, execute the following command:

```bash
python app.py
```

Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Features

The application takes the following inputs:

- **Accident Site**: Select between Parking Lot and Highway.
- **Annual Income**: Enter the annual income.
- **Past Number of Claims**: Enter the number of past claims.
- **High Education Indicator**: Select Yes or No.
- **Witness Present Indicator**: Select Yes or No.
- **Address Change Indicator**: Select Yes or No.
- **Safety Rating**: Enter the safety rating (0 to 5).
- **Claim Estimated Payout**: Enter the estimated payout for the claim.
- **Marital Status**: Select the marital status.
- **Accident Site**: Select the accident site.

The application returns the predicted probability of vehicle insurance fraud based on the provided inputs.

## License

This project is open-source and available under the [MIT License](LICENSE).

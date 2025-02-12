from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")  # Load the same scaler used during training

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Serve the HTML page

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array([
            data["diabetes"], 
            data["History of hypertension (y/n)"], 
            data["Protien Uria"]
        ]).reshape(1, -1)

        # Apply the same scaling as in training
        features_scaled = scaler.transform(features)

        # Predict risk level
        prediction = model.predict(features_scaled)[0]

        # Predict gestational age for high-risk cases
        if prediction == 1:  # High risk
            gestational_age = estimate_gestational_age(features_scaled)
            return jsonify({
                "Risk Level": "High Risk",
                "Estimated Gestational Age": f"{gestational_age} weeks"
            })
        else:
            return jsonify({"Risk Level": "No Risk"})

    except Exception as e:
        return jsonify({"error": str(e)})

def estimate_gestational_age(features_scaled):
    """ Dummy function to estimate gestational age based on model features """
    # Replace this with a regression model trained to predict gestational age
    return int(np.random.randint(24, 36))  # Example: Random 24-36 weeks

if __name__ == "__main__":
    app.run(debug=True)

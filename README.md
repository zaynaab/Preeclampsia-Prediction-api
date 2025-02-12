# Preeclampsia-Prediction-api
# Preeclampsia Risk Prediction Web App

This is a Flask-based web application for predicting the risk level of preeclampsia using a trained XGBoost model. If the predicted risk is high, the app also estimates the gestational age at which preeclampsia is likely to occur.

## Features
- User-friendly web interface for risk prediction
- Uses a pre-trained XGBoost model for accurate predictions
- Estimates gestational age if high risk is detected
- Interactive and colorful UI with a modern design

## Technologies Used
- **Flask** (Backend Framework)
- **XGBoost** (Machine Learning Model)
- **HTML, CSS** (Frontend UI)
- **Joblib** (Model Serialization)
- **Bootstrap & Custom Styling** (Responsive Design)

## Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_USERNAME/Preeclampsia-Prediction-api.git
cd Preeclampsia-Prediction-api
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App
```sh
python app.py
```

The application will start at `http://127.0.0.1:5000/` in your browser.

## API Endpoints
| Method | Endpoint   | Description  |
|--------|-----------|--------------|
| GET    | `/`       | Home page    |
| POST   | `/predict` | Predicts risk level based on input features |

## Deployment
To deploy this app, you can use:
- **Render** (Recommended)
- **Heroku**
- **AWS / Azure / GCP**

### Deploy on Render:
1. Push your code to GitHub
2. Create a new **Web Service** on [Render](https://render.com/)
3. Connect your GitHub repo
4. Set the **Build Command** to:
   ```sh
   pip install -r requirements.txt
   ```
5. Set the **Start Command** to:
   ```sh
   python app.py
   ```
6. Deploy and get your live URL!

## Developed By
**Zainab Bukhari**

If you find this project useful, consider giving it a ⭐ on GitHub!


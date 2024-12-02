from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('svm_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        features = [float(request.form[f'V{i}']) for i in range(1, 29)]
        time = float(request.form['Time'])  # Assuming 'Time' is the missing feature
        amount = float(request.form['Amount'])

        # Combine features into a single array
        input_data = np.array([time] + features + [amount]).reshape(1, -1)

        # Predict
        prediction = model.predict(input_data)
        result = 'Fraudulent' if prediction[0] == 1 else 'Non-Fraudulent'
        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


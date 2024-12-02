# credit_cardd_fraudalent-detection
 A machine learning-based credit card fraud detection system using Flask and an SVM model. The project includes a web API for fraud prediction, Dockerized deployment, and a simple front-end interface for users to input transaction details. It aims to detect fraudulent transactions in real-time.  

 # Project Structure

 credit card frau/
 
├── data/                        # Dataset folder containing creditcard.csv

│   └── creditcard.csv           # The dataset file used for fraud detection

├── notebooks/                   # Jupyter notebooks for EDA & modeling

│   └── EDA.ipynb                # Jupyter notebook for Exploratory Data Analysis (EDA)

├── templates/                   # HTML templates (for front-end)

│   └── index.html               # Main HTML file for the project front-end

├── .dockerignore                # File to specify what to ignore during Docker build

├── .gitattributes               # Git attributes file for defining how Git handles various files

├── .gitignore                   # Git ignore file to exclude files from version control (e.g., data/creditcard.csv)

├── app/                         # Python source file(s) for the application

│   └── app.py                   # Main application logic in Python

├── Dockerfile                   # Instructions for creating the Docker image

├── requirements.txt             # Python dependencies for the project

├── readme.md                    # Project description

└── svm_model.pkl                # Saved model for SVM (Support Vector Machine)


# Features

**Exploratory Data Analysis (EDA):** Performed using a Jupyter notebook to explore and visualize the dataset.

**Model Training**: Built a machine learning model using SVM (Support Vector Machine) to classify transactions as fraudulent or legitimate.

**Deployment**: The model is integrated into a Flask web application for deployment.

**Dockerized Application**: The project is containerized using Docker for easy deployment and scalability.

# Technologies Used

**Python**: For data analysis, machine learning model training, and application development.

**Flask**: To build the web application.

**Jupyter Notebook**: For EDA and data preprocessing.

**Scikit-learn**: For machine learning algorithms.

**Docker**: To containerize the application for easy deployment.

# Getting Started

**Prerequisites**

Before you begin, ensure you have the following installed:

 1. Python 3.x 
 
 2. Docker (for containerization)
 
 3. Git

**Installation**

1. Clone the repository:

   git clone https://github.com/ssprakash1302/credit_cardd_fraudalent-detection.git
   
   cd credit_cardd_fraudalent-detection

2. Install required Python dependencies:

   pip install -r requirements.txt

3. Run the application locally:

   python app/app.py

4. For containerization with Docker:

   Build the Docker image:

   docker build -t credit-card-fraud-detection .

   Run the Docker container:

   docker run -p 5000:5000 credit-card-fraud-detection

5. Using the Web Application

   Open your browser and navigate to http://localhost:5000 to access the app.


**Data Source**

    https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023 

 **Model**

 The machine learning model used in this project is a Support Vector Machine (SVM), which classifies transactions as either fraudulent or legitimate.

 **Contributing**

 If you would like to contribute to this project, feel free to fork the repository and submit pull requests. All contributions are welcome!

 **License**
 
This project is licensed under the MIT License - see the LICENSE file for details.
 

 

 
   
   

   

   


   

   



   



 

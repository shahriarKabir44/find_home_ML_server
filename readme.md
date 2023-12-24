# Find Home ML Server

This project is a web server that predicts whether or not a person is eligible for a loan based on their income, credit score, and other factors. The server uses the http.server library in Python and responds to GET requests with JSON data.

## How it works

The server uses several machine learning models to make predictions, such as logistic regression, decision tree, and random forest. The models are trained on a dataset of loan applicants with their features and labels. The best model is selected based on the accuracy score on a test set. The current best model is a random forest classifier with an accuracy of 76%.

## How to use

To use the server, you need to send a POST request with the following parameters:

-  Maritual Status 
- Dependents 
- Education
- Self_Employed 
- ApplicantIncome_In_Taka 
- CoapplicantIncome_In_Taka 
- LoanAmount_In_Taka
- Loan_Amount_Term
- Credit_History
- Property_Area

The server will respond with a JSON object with the following fields:

{"outcome":0} or {"outcome": 1}
 

## How to run this project
1. **Run it locally**
- Clone the repository:
```bash 
git clone  https://github.com/shahriarKabir44/find_home_ML_server.git
```
- Enter the folder.
- Create a virtial environment 
- to install the dependencies, run 
```bash 
    pip install -r requirements.txt
``` 
- To run the server, 
```bash 
    python server.py
```

Or,

2. **Run the docker image**
- Pull the docker image:
```bash
    sudo docker pull shahriarkabir/find_home_ml_server:latest
```
- Run the image:
```bash
sudo docker run -p <any port>:8080 find_home_ml_server:latest
```


**Conclusion:**
- This repository is a part of the project 
    <a href="https://github.com/shahriarKabir44/findHome">findHome</a>
- We shall try to improve our accuracy by trying out different ML methods
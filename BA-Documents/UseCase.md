# USE CASES

## Use Case 1: User Login

Actor: User

Description: User logs into the system

Pre-condition: User has registered account

Main Flow:

1. User enters username and password
2. System validates credentials
3. System grants access

Post-condition:

- User is logged in

Exception Flow:

- Invalid credentials → Error message

---

## Use Case 2: Upload Dataset

Actor: Bank Analyst

Description: Upload dataset for analysis

Pre-condition:

- User is logged in

Main Flow:

1. User uploads CSV file
2. System validates dataset
3. System processes data
4. System displays results

Post-condition:

- Dataset is processed

Exception Flow:

- Invalid format → Error
- Missing columns → Warning

---

## Use Case 3: Churn Prediction

Actor: Bank Analyst

Description: Predict customer churn

Pre-condition:

- Dataset is uploaded

Main Flow:

1. System processes dataset
2. System predicts churn probability
3. System classifies risk
4. System displays results

Post-condition:

- Prediction available

Exception Flow:

- Invalid dataset → Error

---

## Use Case 4: Customer Segmentation

Actor: Marketing Analyst

Description: Segment customers

Pre-condition:

- Dataset available

Main Flow:

1. User selects features
2. System performs clustering
3. System displays clusters

Post-condition:

- Segments created

Exception Flow:

- Not enough features → Warning

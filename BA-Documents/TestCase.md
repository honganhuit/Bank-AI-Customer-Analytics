# TEST CASES

## 1. Authentication

| TC ID | Scenario         | Preconditions  | Action                    | Expected Result          | Priority | FR  | Status  |
| ----- | ---------------- | -------------- | ------------------------- | ------------------------ | -------- | --- | ------- |
| TC01  | Login success    | User exists    | Submit valid credentials  | Redirect to dashboard    | High     | FR1 | Not Run |
| TC02  | Login failure    | User exists    | Submit invalid password   | Error message displayed  | High     | FR1 | Not Run |
| TC03  | Empty input      | None           | Submit empty form         | Validation message shown | High     | FR1 | Not Run |
| TC04  | Register success | Email not used | Submit valid info         | Account created          | High     | FR1 | Not Run |
| TC05  | Duplicate email  | Email exists   | Submit registration       | Error displayed          | High     | FR1 | Not Run |
| TC06  | Weak password    | None           | Submit invalid password   | Validation fails         | Medium   | FR1 | Not Run |
| TC07  | Reset password   | Email exists   | Submit OTP + new password | Password updated         | High     | FR1 | Not Run |

---

## 2. Dataset Upload & Validation

| TC ID | Scenario            | Preconditions    | Action            | Expected Result               | Priority | FR  | Status  |
| ----- | ------------------- | ---------------- | ----------------- | ----------------------------- | -------- | --- | ------- |
| TC08  | Upload valid CSV    | Logged in        | Upload file       | File loaded successfully      | High     | FR2 | Not Run |
| TC09  | Upload invalid file | Logged in        | Upload non-CSV    | Error message displayed       | High     | FR2 | Not Run |
| TC10  | Large dataset       | Logged in        | Upload large file | System processes successfully | Medium   | FR2 | Not Run |
| TC11  | Empty dataset       | Logged in        | Upload empty file | Warning displayed             | Medium   | FR2 | Not Run |
| TC12  | Missing values      | Dataset uploaded | Run validation    | Warning displayed             | High     | FR3 | Not Run |
| TC13  | Duplicate data      | Dataset uploaded | Run validation    | Duplicate count shown         | Medium   | FR3 | Not Run |
| TC14  | Invalid data type   | Dataset uploaded | Run validation    | Warning displayed             | Medium   | FR3 | Not Run |

---

## 3. Data Analysis

| TC ID | Scenario          | Preconditions         | Action       | Expected Result              | Priority | FR  | Status  |
| ----- | ----------------- | --------------------- | ------------ | ---------------------------- | -------- | --- | ------- |
| TC15  | Generate report   | Valid dataset         | Run analysis | Summary & insights displayed | High     | FR4 | Not Run |
| TC16  | High correlation  | Correlated dataset    | Run analysis | Correlation highlighted      | Medium   | FR4 | Not Run |
| TC17  | Outlier detection | Dataset with outliers | Run analysis | Outliers detected correctly  | Medium   | FR4 | Not Run |

---

## 4. Customer Segmentation

| TC ID | Scenario              | Preconditions    | Action           | Expected Result    | Priority | FR  | Status  |
| ----- | --------------------- | ---------------- | ---------------- | ------------------ | -------- | --- | ------- |
| TC18  | Valid clustering      | Numeric dataset  | Run segmentation | Clusters displayed | High     | FR5 | Not Run |
| TC19  | Insufficient features | Dataset uploaded | Run segmentation | Warning displayed  | High     | FR5 | Not Run |
| TC20  | Non-numeric features  | Dataset uploaded | Run segmentation | Not allowed        | High     | FR5 | Not Run |

---

## 5. Churn Prediction

| TC ID | Scenario             | Preconditions   | Action         | Expected Result        | Priority | FR  | Status  |
| ----- | -------------------- | --------------- | -------------- | ---------------------- | -------- | --- | ------- |
| TC21  | Valid prediction     | Valid dataset   | Run prediction | Risk results displayed | High     | FR6 | Not Run |
| TC22  | Feature mismatch     | Invalid dataset | Run prediction | Error displayed        | High     | FR6 | Not Run |
| TC23  | Missing numeric data | Invalid dataset | Run prediction | Process stopped        | High     | FR6 | Not Run |

---

## 6. Dashboard & Export

| TC ID | Scenario          | Preconditions     | Action         | Expected Result           | Priority | FR  | Status  |
| ----- | ----------------- | ----------------- | -------------- | ------------------------- | -------- | --- | ------- |
| TC24  | View dashboard    | Data processed    | Open dashboard | Charts render correctly   | High     | FR7 | Not Run |
| TC25  | Download CSV      | Results available | Click download | File downloaded           | High     | FR7 | Not Run |
| TC26  | Risk distribution | Prediction done   | View chart     | Chart displayed correctly | Medium   | FR7 | Not Run |

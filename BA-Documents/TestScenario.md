# TEST SCENARIOS

## 1. Authentication

| Test ID | Test Case     | Input                   | Expected Result             |
| ------- | ------------- | ----------------------- | --------------------------- |
| TC01    | Login success | Valid username/password | User logged in successfully |
| TC02    | Login failure | Invalid credentials     | Error message displayed     |
| TC03    | Empty input   | Empty fields            | Validation message shown    |

---

## 2. Dataset Upload & Validation

| Test ID | Test Case           | Input           | Expected Result           |
| ------- | ------------------- | --------------- | ------------------------- |
| TC04    | Upload valid CSV    | Correct format  | File accepted             |
| TC05    | Upload invalid file | Non-CSV file    | Error message displayed   |
| TC06    | Missing columns     | Incomplete data | Validation warning        |
| TC07    | Duplicate records   | Duplicate rows  | System detects duplicates |

---

## 3. Data Analysis

| Test ID | Test Case           | Input            | Expected Result        |
| ------- | ------------------- | ---------------- | ---------------------- |
| TC08    | Generate statistics | Valid data       | Summary displayed      |
| TC09    | Detect outliers     | Data w/ outliers | Outliers identified    |
| TC10    | Correlation check   | Valid data       | High correlation shown |

---

## 4. Customer Segmentation

| Test ID | Test Case           | Input           | Expected Result    |
| ------- | ------------------- | --------------- | ------------------ |
| TC11    | Run segmentation    | Numeric dataset | Clusters generated |
| TC12    | Not enough features | <2 features     | Warning displayed  |

---

## 5. Churn Prediction

| Test ID | Test Case        | Input              | Expected Result        |
| ------- | ---------------- | ------------------ | ---------------------- |
| TC13    | Run prediction   | Valid dataset      | Risk results displayed |
| TC14    | Feature mismatch | Wrong feature size | Error message          |

---

## 6. Output & Export

| Test ID | Test Case       | Input          | Expected Result     |
| ------- | --------------- | -------------- | ------------------- |
| TC15    | Download result | Click download | CSV file downloaded |
| TC16    | View dashboard  | Valid data     | Charts displayed    |

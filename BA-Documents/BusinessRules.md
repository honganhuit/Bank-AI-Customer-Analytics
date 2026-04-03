# BUSINESS RULES

## 1. Authentication Rules

- Only authenticated users can access system features
- Email must be unique in the system
- Password must:
  - Have at least 4 characters
  - Contain at least one letter and one number
- OTP is required for password reset and must be valid

---

## 2. Data Validation Rules

- System only accepts CSV files
- Dataset must contain required features for analysis and prediction
- System must detect:
  - Missing values
  - Duplicate records
  - Invalid data types

---

## 3. Data Analysis Rules

- Only numeric columns are used for statistical analysis
- Correlation threshold for high correlation is > 0.8
- Outliers are defined as values outside mean ± 2 \* standard deviation

---

## 4. Segmentation Rules

- Minimum 2 numeric features required
- Only numeric data is used for clustering
- Default number of clusters = 3

---

## 5. Churn Prediction Rules

- Input dataset must match model feature requirements
- Risk classification:
  - High Risk: probability > 0.7
  - Medium Risk: 0.4 ≤ probability ≤ 0.7
  - Low Risk: probability < 0.4

---

## 6. Output Rules

- Results must be displayed in dashboard format
- Users can export results as CSV file
- System must show clear error messages for invalid inputs

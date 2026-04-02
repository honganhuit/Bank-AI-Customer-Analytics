# SYSTEM REQUIREMENT DOCUMENT (SRD)

## 1. Introduction

### 1.1 Purpose

Define system-level requirements for ATBank AI Customer Analytics system.

---

## 2. System Overview

### 2.1 Architecture

- Frontend: Streamlit
- Backend: Python (Pandas, NumPy)
- ML Model: ONNX Runtime
- Database: SQLite

---

## 3. Functional Requirements

### FR1: Authentication

- Register account
- Login / Logout
- Validate email format
- Password rules:
  - ≥ 4 characters
  - Contains letters and numbers
- Reset password via OTP

---

### FR2: Dataset Upload

- Accept CSV only
- Display dataset preview
- Show row/column count

---

### FR3: Data Validation

- Detect missing values
- Detect duplicates
- Identify data types

---

### FR4: Data Analysis

- Calculate mean, median, std
- Detect skewness
- Detect outliers (mean ± 2\*std)
- Detect correlation > 0.8
- Generate AI report

---

### FR5: Data Visualization

- Histogram
- Boxplot
- Heatmap
- Missing values chart

---

### FR6: Customer Segmentation

- K-Means clustering
- Numeric features only
- Minimum 2 features
- Output cluster labels

---

### FR7: Churn Prediction

- Load ONNX model
- Validate feature count
- Predict churn probability

---

### FR8: Risk Classification

- High Risk: > 0.7
- Medium Risk: 0.4 – 0.7
- Low Risk: < 0.4

---

### FR9: Dashboard

- Dataset overview
- Statistical summary
- Risk distribution
- Top 10 risky customers
- AI insights

---

### FR10: Export

- Download CSV file

---

## 4. Non-Functional Requirements

### Performance

- Process within ~5 seconds

### Usability

- Simple UI

### Security

- Password validation
- OTP reset
- Session handling

### Reliability

- Handle errors gracefully

### Scalability

- Support medium datasets

---

## 5. Data Requirements

### Input

- CSV format
- Numeric features required

### Output

- Dataset with:
  - Cluster
  - Churn Probability
  - Risk Level

---

## 6. Constraints

- Requires ONNX model
- No real-time processing
- No external integration

---

## 7. Assumptions

- Dataset is valid
- User understands basic data
- Email system works

---

## 8. Error Handling

- Invalid file → error
- Missing data → warning
- Model mismatch → stop
- Login fail → error

---

## 9. Success Criteria

- Prediction works correctly
- Dashboard displays correctly
- Export works
- No major errors

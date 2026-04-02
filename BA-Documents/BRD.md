# BUSINESS REQUIREMENT DOCUMENT (BRD)

## 1. Project Overview

ATBank AI Customer Analytics is a business-oriented system designed to support banking analysts in analyzing customer data, predicting churn risk, and identifying customer segments.

The system enables users to upload customer datasets (CSV), perform automated data analysis, and generate actionable insights to support data-driven decision-making.

---

## 2. Business Objectives

- Reduce customer churn by identifying high-risk customers
- Support data-driven decision-making through automated insights
- Improve customer segmentation for targeted marketing strategies
- Enhance efficiency in analyzing large customer datasets

---

## 3. Scope

### 3.1 In Scope

- Upload and process customer datasets (CSV format)
- Data validation (missing values, duplicates, incorrect format)
- Feature validation for machine learning model input
- Automated data analysis and statistical insights
- AI-generated data analysis report
- Data visualization:
  - Histogram (distribution)
  - Boxplot (outlier detection)
  - Correlation heatmap
  - Missing values chart

- Customer segmentation using K-Means clustering
- Customer churn prediction using pre-trained ML model (ONNX)
- Risk classification (High / Medium / Low)
- Export analysis results (CSV download)
- User account management:
  - Register
  - Login / Logout
  - Change username/password
  - Reset password via OTP email

---

### 3.2 Out of Scope

- Real-time data streaming and processing
- Integration with core banking systems or CRM
- Model retraining or customization by end users
- Role-based access control (Admin vs User)

---

## 4. Stakeholders

- **Bank Analyst** – primary user performing analysis and churn prediction
- **Marketing Team** – uses segmentation results for campaigns
- **Business Manager** – uses insights for strategic decision-making
- **System Administrator (implicit)** – manages system and user data

---

## 5. User Roles

| Role             | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| User             | Upload dataset, analyze data, view dashboard, download results |
| Admin (implicit) | Maintain system and user data (not implemented UI)             |

---

## 6. High-Level Workflow

User Login
→ Upload Dataset (CSV)
→ Data Validation
→ Data Analysis & AI Report
→ Data Visualization
→ Customer Segmentation
→ Churn Prediction
→ Risk Classification
→ Dashboard Display
→ Export Results (CSV)

---

## 7. Functional Requirements

### 7.1 Authentication

- User can register with username, email, and password
- System validates email format
- Password must meet rules:
  - Minimum 4 characters
  - Contains letters and numbers

- User can login with valid credentials
- User can logout
- User can update username and password
- User can reset password via OTP sent to email

---

### 7.2 Data Upload & Validation

- System accepts CSV files only
- System reads dataset and displays preview
- System validates:
  - Missing values
  - Duplicate rows
  - Data types (numeric / non-numeric)

- System removes unnecessary columns for model (e.g., CustomerId, Surname)
- System checks number of features required by ML model

---

### 7.3 Data Analysis

- System generates statistical summary:
  - Mean
  - Median
  - Standard deviation

- System identifies:
  - Data distribution (skewness)
  - Outliers (mean ± 2\*std)

- System detects high correlation between variables (> 0.8)
- System generates AI-based textual insights and recommendations

---

### 7.4 Data Visualization

- System displays:
  - Histogram for feature distribution
  - Boxplot for outlier detection
  - Correlation heatmap
  - Missing values bar chart

- User can select features for visualization

---

### 7.5 Customer Segmentation

- System performs clustering using K-Means
- Only numeric features are used
- Minimum 2 features required
- Default number of clusters: 3
- System displays cluster visualization (scatter plot)

---

### 7.6 Churn Prediction

- System loads pre-trained ONNX model
- System processes dataset input
- System predicts churn probability for each customer
- System adds:
  - Churn Probability
  - Risk Level

#### Risk Classification Rules:

- High Risk: probability > 0.7
- Medium Risk: 0.4 ≤ probability ≤ 0.7
- Low Risk: probability < 0.4

---

### 7.7 Reporting & Export

- System displays results in dashboard
- System shows:
  - Risk distribution (pie chart)
  - Top 10 high-risk customers

- System allows exporting results as CSV file

---

## 8. Non-Functional Requirements

- **Performance:**
  - Data processing should complete within ~5 seconds for medium datasets

- **Usability:**
  - Simple and intuitive UI (Streamlit-based dashboard)

- **Security:**
  - Password validation rules applied
  - OTP verification for password reset
  - Session-based authentication

- **Reliability:**
  - System handles invalid input gracefully
  - Error messages displayed clearly

- **Scalability:**
  - Supports moderate dataset sizes (not big data)

---

## 9. Business Rules

### 9.1 Authentication Rules

- Only registered users can access the system
- Email must be unique
- Password must follow validation rules
- OTP must be valid for password reset

---

### 9.2 Data Rules

- Only CSV format is accepted
- Dataset must contain required numeric features
- System detects missing and duplicate data
- Only numeric columns are used for:
  - Segmentation
  - Prediction

---

### 9.3 Prediction Rules

- Input features must match model requirements
- If insufficient features → system shows error
- Risk classification:
  - High Risk: > 0.7
  - Medium Risk: 0.4 – 0.7
  - Low Risk: < 0.4

---

### 9.4 Output Rules

- Results must be displayed clearly in dashboard
- Users can download results as CSV
- System highlights high-risk customers

---

## 10. Assumptions

- Users have basic knowledge of data analysis
- Input datasets are structured and valid
- Machine learning model is pre-trained and available
- Email service is functioning for OTP delivery

---

## 11. Constraints

- System depends on ONNX pre-trained model
- No real-time processing capability
- Limited to offline dataset analysis
- No role-based access control implemented

---

## 12. Success Criteria

- Users can upload and analyze datasets successfully
- System generates churn predictions without errors
- Users can identify high-risk customers
- Insights support business decision-making
- System improves efficiency compared to manual analysis

---

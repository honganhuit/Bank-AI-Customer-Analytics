# FUNCTIONAL SPECIFICATION DOCUMENT (FSD)

## 1. Overview

This document describes the detailed functional behavior of the ATBank AI Customer Analytics system, including user interactions, processing logic, business rules, and system outputs.

---

## 2. System Modules

- Authentication
- Dataset Management
- Data Validation
- Data Analysis
- Data Visualization
- Customer Segmentation
- Churn Prediction
- Dashboard & Reporting
- Export

---

## 3. Feature Specifications

---

## 3.1 Authentication Module

### 3.1.1 Login

**Input**

- Username
- Password

**UI Behavior**

- User enters credentials and clicks **Login**
- System displays loading indicator

**Processing Logic**

1. Validate input (non-empty)
2. Check credentials from database
3. Create session if valid

**Business Rules**

- Username and password must not be empty
- Invalid credentials → deny access

**Output**

- Success → Redirect to Dashboard
- Failure → Show error message

---

### 3.1.2 Register

**Input**

- Username
- Email
- Password

**Processing Logic**

1. Validate email format
2. Validate password rules
3. Check duplicate email
4. Save user to database

**Business Rules**

- Email must be unique
- Password must contain letters and numbers

**Output**

- Success → Account created
- Failure → Validation error message

---

### 3.1.3 Reset Password (OTP)

**Flow**

1. User enters email
2. System sends OTP
3. User inputs OTP and new password

**Rules**

- OTP must be valid
- OTP expires after a defined time

**Output**

- Password updated successfully
- Error if OTP is invalid

---

## 3.2 Dataset Upload Module

**Input**

- CSV file

**UI Behavior**

- File upload component
- Display dataset preview after upload

**Processing Logic**

1. Validate file format (CSV only)
2. Read file into dataset
3. Display:
   - Number of rows
   - Number of columns

**Validation Rules**

- Non-CSV → error
- Empty file → warning
- Corrupted file → error

**Output**

- Dataset preview
- Validation messages

---

## 3.3 Data Validation Module

**Processing Logic**

1. Detect missing values
2. Detect duplicate rows
3. Identify data types

**Business Rules**

- Missing values → warning (non-blocking)
- Duplicate rows → show count
- Invalid data types → warning

**Output**

- Validation summary:
  - Missing values count
  - Duplicate count
  - Data type overview

---

## 3.4 Data Analysis Module

**UI Behavior**

- User clicks **Analyze Data**

**Processing Logic**

1. Generate statistical summary:
   - Mean
   - Median
   - Standard deviation
2. Detect:
   - Outliers
   - Correlation
3. Generate insights report

**Business Rules**

- Only numeric columns are processed
- No numeric data → disable analysis

**Output**

- Statistical summary table
- Insight report

---

## 3.5 Data Visualization Module

**UI Behavior**

- User selects features for visualization

**Supported Charts**

- Histogram
- Boxplot
- Correlation heatmap
- Missing values chart

**Rules**

- Only numeric features allowed
- No selection → show message

**Output**

- Charts displayed on dashboard

---

## 3.6 Customer Segmentation Module

**Input**

- Selected numeric features

**UI Behavior**

- Feature selection dropdown
- Button: **Run Segmentation**

**Processing Logic**

1. Validate selected features
2. Apply clustering algorithm
3. Assign cluster labels

**Business Rules**

- Minimum 2 features required
- Only numeric data allowed

**Output**

- Dataset with Cluster column
- Visualization chart

**Error Handling**

- Insufficient features → warning
- Invalid data → stop process

---

## 3.7 Churn Prediction Module

**Input**

- Processed dataset

**UI Behavior**

- Button: **Predict Churn**

**Processing Logic**

1. Validate input features
2. Load prediction model
3. Run inference
4. Generate probability
5. Classify risk level

**Business Rules**

- Input must match model structure
- Missing features → stop prediction

**Output**

- Churn Probability
- Risk Level

**Error Handling**

- Model error → show message
- Feature mismatch → stop execution

---

## 3.8 Dashboard Module

**UI Components**

- Dataset overview
- Statistical summary
- Risk distribution chart
- Top high-risk customers
- Insight panel

**Behavior**

- Auto-update after each process
- Highlight high-risk customers

---

## 3.9 Export Module

**UI Behavior**

- Button: **Download CSV**

**Processing Logic**

1. Prepare dataset including:
   - Original data
   - Cluster
   - Churn Probability
   - Risk Level
2. Generate CSV file

**Output**

- Downloadable file

**Error Handling**

- No data → disable export button

---

## 4. Global Error Handling

| Scenario         | System Behavior             |
| ---------------- | --------------------------- |
| Invalid file     | Show error message          |
| Empty dataset    | Show warning                |
| Feature mismatch | Stop process                |
| Model error      | Show error                  |
| System failure   | Log error and prevent crash |

---

## 5. User Flow

Login  
→ Dashboard  
→ Upload Dataset  
→ Validate Data  
→ Analyze Data  
→ Visualize  
→ Segment Customers  
→ Predict Churn  
→ View Results  
→ Export Data

---

## 6. Notes for Development

- Processing time should be under 5 seconds for medium datasets
- UI should remain simple and intuitive
- All errors must be handled gracefully
- System should not crash on invalid input

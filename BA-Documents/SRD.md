# SYSTEM REQUIREMENT DOCUMENT (SRD)

## 1. Introduction

### 1.1 Purpose

Define system-level requirements for ATBank AI Customer Analytics system.

---

## 2. Functional Requirements

### FR1: User Authentication

- FR1.1: System allows users to register with username, email, and password
- FR1.2: System allows users to login with valid credentials
- FR1.3: System allows password reset via OTP verification
- FR1.4: System allows users to update username and password

---

### FR2: Dataset Upload & Validation

- FR2.1: System allows users to upload CSV files
- FR2.2: System validates file format and structure
- FR2.3: System detects missing values and duplicate records
- FR2.4: System validates required features for processing

---

### FR3: Data Analysis

- FR3.1: System generates statistical summary
- FR3.2: System detects outliers
- FR3.3: System identifies correlation between variables
- FR3.4: System generates automated insights report

---

### FR4: Data Visualization

- FR4.1: System displays data distribution charts
- FR4.2: System displays outlier visualization
- FR4.3: System displays correlation heatmap
- FR4.4: System displays missing values chart

---

### FR5: Customer Segmentation

- FR5.1: System allows feature selection
- FR5.2: System performs customer segmentation
- FR5.3: System displays segmentation results visually

---

### FR6: Churn Prediction

- FR6.1: System predicts churn probability
- FR6.2: System classifies risk levels (High / Medium / Low)
- FR6.3: System displays prediction results

---

### FR7: Reporting & Export

- FR7.1: System displays analysis results in dashboard
- FR7.2: System allows users to download results as CSV
- FR7.3: System highlights high-risk customers

---

## 3. Non-Functional Requirements

### Performance

- System should process datasets within 5 seconds for standard size

### Security

- User authentication is required
- Password must be validated
- OTP verification is required for password reset

### Usability

- System interface should be simple and user-friendly
- Users can perform tasks without technical knowledge

### Reliability

- System handles invalid inputs with appropriate error messages
- System prevents crashes during processing

### Scalability

- System supports increasing dataset size within reasonable limits

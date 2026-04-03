# USER STORIES & ACCEPTANCE CRITERIA

## EPIC: Customer Analytics System

---

## US1: Upload & Validate Dataset

**As a** bank analyst  
**I want** to upload a customer dataset  
**So that** I can analyze customer data for insights

### Acceptance Criteria

- **AC1 – Upload valid file**
  - Given user is logged in
  - When user uploads a valid CSV file
  - Then system accepts file and displays dataset preview

- **AC2 – Invalid file format**
  - Given user uploads a non-CSV file
  - When system processes file
  - Then error message is displayed

- **AC3 – Data validation**
  - Given dataset is uploaded
  - When validation runs
  - Then system detects:
    - Missing values
    - Duplicate records
    - Invalid data types

- **AC4 – Empty dataset**
  - Given dataset has 0 rows
  - When validation runs
  - Then system shows warning

---

## US2: Data Analysis & Insights

**As a** data analyst  
**I want** automated data analysis  
**So that** I can quickly understand patterns and issues

### Acceptance Criteria

- **AC1 – Generate summary**
  - Given dataset is valid
  - When user runs analysis
  - Then system displays statistical summary

- **AC2 – Detect outliers**
  - Given dataset contains outliers
  - When analysis runs
  - Then outliers are identified

- **AC3 – Correlation detection**
  - Given dataset has correlated features
  - When analysis runs
  - Then high correlation is highlighted

- **AC4 – Insights report**
  - Given analysis is completed
  - When report is generated
  - Then system displays insights and recommendations

---

## US3: Customer Segmentation

**As a** marketing analyst  
**I want** to segment customers  
**So that** I can target marketing campaigns effectively

### Acceptance Criteria

- **AC1 – Valid segmentation**
  - Given dataset has numeric features
  - When user selects features and runs segmentation
  - Then clusters are generated

- **AC2 – Feature validation**
  - Given less than 2 features selected
  - When user runs segmentation
  - Then system shows warning

- **AC3 – Data type validation**
  - Given selected features are non-numeric
  - When user runs segmentation
  - Then system prevents execution

- **AC4 – Visualization**
  - Given segmentation completed
  - When results are displayed
  - Then system shows cluster visualization

---

## US4: Churn Prediction

**As a** bank analyst  
**I want** to predict customer churn risk  
**So that** I can identify high-risk customers

### Acceptance Criteria

- **AC1 – Valid prediction**
  - Given dataset is valid
  - When user runs prediction
  - Then system displays churn probability

- **AC2 – Risk classification**
  - Given prediction is completed
  - When results are generated
  - Then system classifies risk levels:
    - High
    - Medium
    - Low

- **AC3 – Feature mismatch**
  - Given dataset does not match required features
  - When prediction runs
  - Then system shows error

---

## US5: Dashboard Visualization

**As a** user  
**I want** to view analysis results visually  
**So that** I can easily understand insights

### Acceptance Criteria

- **AC1 – Display charts**
  - Given analysis is completed
  - When user opens dashboard
  - Then charts are displayed:
    - Distribution charts
    - Correlation heatmap
    - Risk distribution

- **AC2 – High-risk highlight**
  - Given prediction results exist
  - When dashboard loads
  - Then high-risk customers are highlighted

---

## US6: Export Results

**As a** user  
**I want** to download analysis results  
**So that** I can use data outside the system

### Acceptance Criteria

- **AC1 – Export CSV**
  - Given results are available
  - When user clicks download
  - Then CSV file is downloaded

- **AC2 – Data completeness**
  - Given export file is generated
  - When user opens file
  - Then file contains:
    - Original data
    - Churn probability
    - Risk level
    - Cluster

---

## US7: User Authentication

**As a** user  
**I want** secure access to the system  
**So that** my data is protected

### Acceptance Criteria

- **AC1 – Login success**
  - Given valid credentials
  - When user logs in
  - Then access is granted

- **AC2 – Login failure**
  - Given invalid credentials
  - When user logs in
  - Then error message is shown

- **AC3 – Register**
  - Given valid information
  - When user registers
  - Then account is created

- **AC4 – Reset password**
  - Given user requests password reset
  - When OTP is valid
  - Then password is updated

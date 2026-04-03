# REQUIREMENTS TRACEABILITY MATRIX (RTM)

## Overview

This document ensures full traceability between business requirements, system functionalities, use cases, and test cases.  
It helps verify that all requirements are implemented and properly tested.

---

## RTM Table

| Business Requirement  | Functional Requirement        | Use Case          | Test Case                       | Description                                               | Priority | Status |
| --------------------- | ----------------------------- | ----------------- | ------------------------------- | --------------------------------------------------------- | -------- | ------ |
| User Authentication   | User can register account     | User Registration | Valid/Invalid input tests       | Allow new users to create account with email and password | High     | Done   |
| User Authentication   | User can login system         | User Login        | Login success/failure tests     | Authenticate user credentials and grant access            | High     | Done   |
| User Authentication   | User can reset password       | Forgot Password   | OTP verification tests          | Allow users to reset password via email OTP               | High     | Done   |
| Data Upload           | Upload dataset (CSV)          | Upload Dataset    | File upload validation tests    | User uploads dataset for analysis                         | High     | Done   |
| Data Validation       | Validate dataset structure    | Validate Data     | Missing column / datatype tests | Ensure dataset meets required schema                      | High     | Done   |
| Data Analysis         | Generate statistical analysis | Analyze Data      | Data summary tests              | Compute statistics (mean, median, std)                    | Medium   | Done   |
| Data Visualization    | Display charts and graphs     | View Dashboard    | Chart rendering tests           | Show histogram, boxplot, correlation heatmap              | Medium   | Done   |
| Customer Segmentation | Cluster customers             | Segmentation      | Clustering result tests         | Group customers using KMeans algorithm                    | Medium   | Done   |
| Churn Prediction      | Predict churn probability     | Predict Churn     | Model prediction tests          | Predict customer churn using ML model                     | High     | Done   |
| Risk Classification   | Classify customer risk level  | View Risk Level   | Threshold validation tests      | Categorize customers into High/Medium/Low risk            | High     | Done   |
| Dashboard             | Display analytics dashboard   | View Dashboard    | UI display tests                | Show metrics, dataset overview, insights                  | Medium   | Done   |
| Export Results        | Export analysis results       | Export Data       | File export tests               | Allow users to download results as CSV                    | Medium   | Done   |

---

## Notes

- Each business requirement is mapped to at least one functional requirement
- All functional requirements are covered by test cases
- Ensures no missing or untested functionality in the system

---

## Conclusion

The RTM ensures that all requirements are traceable, implemented, and validated through testing, reducing risks and improving system quality.

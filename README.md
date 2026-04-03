# ATBank AI Customer Analytics

## 1. Project Overview

ATBank AI Customer Analytics is a business-oriented system designed to support customer churn prediction, data analysis, and customer segmentation.

The system helps analysts and business users make data-driven decisions through structured workflows and insights.

---

## 2. Business Objectives

- Reduce customer churn rate
- Support data-driven decision-making
- Identify high-value and high-risk customers
- Improve customer segmentation for marketing strategies

---

## 3. Scope

### 3.1 In Scope

- Customer churn prediction using machine learning models
- Customer data analysis and insights generation
- Customer segmentation based on behavioral and demographic data
- User account management (registration, login, authentication)

### 3.2 Out of Scope

- Real-time data processing
- Integration with external banking systems

---

## 4. My Role – Business Analyst

In this project, I performed the role of a Business Analyst:

- Gathered and analyzed business requirements to define system objectives
- Defined functional and non-functional requirements to ensure system completeness
- Designed business workflows and user flows to support user activities
- Defined business rules and acceptance criteria for system validation
- Created BA documents (BRD, User Stories, Use Cases) for clear communication
- Supported SIT/UAT and validated system outputs against business expectations

---

## 5. BA Deliverables

The following Business Analysis artifacts were created:

- Business Requirement Document (BRD)
- User Stories and Use Cases
- Functional and Non-functional Requirements
- Process Flow Diagram
- Test Scenarios and Validation Rules

All documents are available in:

/BA-Documents/

---

## 6. Business Workflow

User Login  
→ Upload Dataset  
→ Validate Data  
→ Analyze Data  
→ Perform Customer Segmentation  
→ Predict Churn Risk  
→ Display Results  
→ Export Data

---

## 7. Key Business Rules

- Dataset must contain required fields
- Data must be in correct format

Churn risk classification:

- High: > 0.7
- Medium: 0.4 – 0.7
- Low: < 0.4

---

## 8. Technical Implementation (Supporting Layer)

- Frontend: Streamlit
- Backend: Python
- Machine Learning: Churn prediction model (ONNX)
- Database: SQLite

---

## 9. Repository Structure

/
├── BA-Documents/  
│ → Business Analysis artifacts (BRD, User Stories, Use Cases, Test Scenarios, etc.)  
│  
├── ATBank_Full_Diagrams/  
│ ├── banking-system_user-flow.png  
│ ├── banking-system_user-flow.drawio  
│ ├── Business process flow for churn prediction.png  
│ ├── Customer analysts system diagrams.png
│ └── Customer analysts system.png
│  
├── app.py  
├── KHTUBODV2.ipynb  
├── database.py  
├── email_utils.py  
├── rf_model.onnx  
├── test.csv  
├── KHTUBDV2.ipynb  
├── requirements.txt  
├── runtime.txt  
├── .gitignore  
└── README.md

---

## 10. How to Run

git clone https://github.com/honganhuit/ATBank-AI-Customer-Analytics.git  
cd ATBank-AI-Customer-Analytics

pip install -r requirements.txt  
streamlit run app.py

---

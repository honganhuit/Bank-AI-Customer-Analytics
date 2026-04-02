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

- Customer churn prediction
- Data analysis and insights generation
- Customer segmentation
- User account management

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
`/BA-Documents/`

---

## 6. Business Workflow

The system follows the workflow below:

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
- Churn risk classification:
  - High: > 0.7
  - Medium: 0.4 – 0.7
  - Low: < 0.4

---

## 8. Technical Implementation (Supporting Layer)

- Python, Streamlit
- Machine Learning models
- SQLite database

---

## 9. Repository Structure

/
│
├── BA-Documents/
│ → Business Analysis artifacts (BRD, User Stories, Use Cases, Test Scenarios, etc.)
│
├── ATBank_Full_Diagrams/
│
│ ├── banking-system_user-flow.png
│ │ → Business workflow diagram (viewable image)
│ │
│ ├── banking-system_user-flow.drawio
│ │ → Editable workflow design
│ │ Business process flow for churn prediction
│ │
│ ├── use-case-diagram.drawio
│ │ → Editable Use Case diagram for platform
│ │
│ ├── activity-diagram.drawio
│ │ → Editable Activity diagram (Main flow)
│ │
│ ├── sequence-diagram.drawio
│ │ → Editable Sequence diagram (Churn Prediction flow)
│ │
│ └── system-architecture.drawio
│ → Editable System Architecture diagram
│
├── app.py
│ → Main application (supporting implementation)
│
├── database.py
│ → Database operations
│
├── email_utils.py
│ → Email and notification handling
│
├── rf_model.onnx
│ → Machine learning model for churn prediction
│
├── test.csv
│ → Sample dataset for testing
│
├── KHTUBDV2.ipynb
│ → Data exploration and model development
│
├── requirements.txt
│ → Project dependencies
│
├── runtime.txt
│ → Runtime configuration
│
├── .gitignore
│ → Git ignore rules
│
└── README.md
→ Project overview and documentation

# 🏦 ATBank AI Customer Analytics

AI-powered banking analytics platform for **customer churn prediction, automatic data insights, and customer segmentation**.  
This platform demonstrates end-to-end **data science workflow** with **interactive dashboards**, helping analysts and bank managers make data-driven decisions.

Built with **Python, Streamlit, Machine Learning, ONNX, and Plotly**.

---

## 🎯 Goal

- Predict potential **customer churn** using historical banking data.
- Provide **automatic data insights** for quick anomaly detection.
- Perform **customer segmentation** to identify high-value and risky customers.
- Offer an **interactive dashboard** for business analytics.

---

## 👤 User Stories & Use Cases

### **User Story 1: Churn Prediction**

- **As a** bank analyst
- **I want to** upload a customer dataset
- **So that** I can identify customers at risk of leaving the bank.

**Use Case (Simplified Flow):**

1. Login to the system
2. Upload customer dataset (CSV)
3. System validates dataset and detects missing/duplicate values
4. AI model predicts churn probability (RandomForest ONNX model)
5. System displays churn probabilities and risk levels (High/Medium/Low)
6. User can export predictions (CSV)

**Exceptions / Alternate Flows:**

- Dataset with missing critical columns → Show error
- Dataset with incompatible feature count → Show warning

---

### **User Story 2: Automatic Data Insights**

- **As a** data analyst
- **I want to** receive automated analysis of the dataset
- **So that** I can quickly identify anomalies and patterns.

**Use Case (Simplified Flow):**

1. Upload dataset
2. System generates insights:
   - Outliers detection
   - Skewness and distribution analysis
   - Missing value summary
   - High correlation detection
3. Insights are displayed with recommendations for preprocessing or further analysis

---

### **User Story 3: Customer Segmentation**

- **As a** marketing analyst
- **I want to** cluster customers
- **So that** I can identify high-value and risky customer segments.

**Use Case (Simplified Flow):**

1. Select numeric features for clustering
2. System runs **K-Means clustering**
3. Displays clusters in an interactive scatter plot
4. Export cluster assignments for business actions

---

### **User Story 4: Account Management**

- **As a** platform user
- **I want to** manage my account securely
- **So that** I can login, reset, and change my password safely.

**Use Case (Simplified Flow):**

1. User login / registration
2. Forgot password → OTP verification via email -> Reset password
3. Update username or password
4. System enforces password strength rules

---

## 📊 Workflow Overview

1. **User Login / Registration** -> Secure authentication
2. **Upload Customer Dataset** -> CSV input
3. **Automatic Data Analysis** -> Outliers, missing values, correlations, distribution
4. **Customer Segmentation** -> K-Means clustering visualization
5. **Churn Prediction** → RandomForest ONNX model
6. **Results Display & Export** -> Risk levels, CSV download
7. **Visualization Dashboard** -> Interactive charts and metrics

**Validation Rules:**

- Required fields present in dataset
- Correct data types
- Minimum feature requirement for AI model
- Email/password validation for user accounts

---

## 🛠 Key Technologies

- **Web & UI:** Python, Streamlit
- **Data Science & ML:** Pandas, NumPy, Scikit-learn, ONNX Runtime
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Database:** SQLite for user accounts and data storage
- **Email & Utilities:** smtplib, dotenv for OTP and password reset

---

## ⚙️ How to Run

1. Clone repository:

```bash
git clone https://github.com/honganhuit/Bank-AI-Customer-Analytics.git
cd Bank-AI-Customer-Analytics
```

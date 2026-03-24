import streamlit as st
import uuid
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np
import onnxruntime as ort
import plotly.express as px
from sklearn.cluster import KMeans

import database as db
from email_utils import send_email


MODEL_PATH = "rf_model.onnx"

st.set_page_config(page_title="ATBank System", layout="wide")

db.create_tables()


if "page" not in st.session_state:
    st.session_state.page = "Login"

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = ""


if "reset_step" not in st.session_state:
    st.session_state.reset_step = 1

if "reset_user" not in st.session_state:
    st.session_state.reset_user = ""


def ai_generate_report(df):

    report = []

    rows, cols = df.shape
    report.append(f"Dataset có {rows} dòng và {cols} cột.")

    numeric = df.select_dtypes(include=np.number)

    if len(numeric.columns) > 0:

        report.append("\n📊 Thống kê quan trọng:")

        for col in numeric.columns:

            mean = numeric[col].mean()
            median = numeric[col].median()
            std = numeric[col].std()

            report.append(
                f"- {col}: mean={mean:.2f}, median={median:.2f}, std={std:.2f}"
            )

            if mean > median:
                report.append(f"  → {col} có xu hướng lệch phải")

            if mean < median:
                report.append(f"  → {col} có xu hướng lệch trái")

    # Missing values

    missing = df.isnull().sum().sum()

    if missing > 0:
        report.append(f"\n⚠ Dataset có {missing} giá trị thiếu")

    # Duplicate

    dup = df.duplicated().sum()

    if dup > 0:
        report.append(f"\n⚠ Dataset có {dup} dòng trùng")

    # Correlation insight

    if len(numeric.columns) >= 2:

        corr = numeric.corr().abs()

        high_corr = []

        for i in corr.columns:
            for j in corr.columns:

                if i != j and corr.loc[i, j] > 0.8:

                    high_corr.append(f"{i} và {j}")

        if high_corr:

            report.append("\n🔥 Các biến có tương quan cao:")
            report += high_corr[:5]

    # Outlier detection

    outlier_cols = []

    for col in numeric.columns:

        mean = numeric[col].mean()
        std = numeric[col].std()

        outliers = numeric[numeric[col] > mean + 2 * std]

        if len(outliers) > 0:

            outlier_cols.append(f"{col} ({len(outliers)} giá trị bất thường)")

    if outlier_cols:

        report.append("\n🚨 Phát hiện outliers:")
        report += outlier_cols

    # Recommendation

    report.append("\n💡 Gợi ý phân tích:")

    report.append("- Kiểm tra các cột có outlier")
    report.append("- Chuẩn hóa dữ liệu trước khi train model")
    report.append("- Xem xét correlation để tránh multicollinearity")

    return "\n".join(report)


# ================= STATISTIC EXPLAIN =================
def explain_statistics(df):

    numeric = df.select_dtypes(include=np.number)

    explanations = []

    for col in numeric.columns:

        mean = numeric[col].mean()
        median = numeric[col].median()
        std = numeric[col].std()

        text = f"""
### {col}

Mean: {mean:.2f}  
Median: {median:.2f}  
Std: {std:.2f}

"""

        # giải thích mean
        text += f"Trung bình của {col} là **{mean:.2f}**.\n\n"

        # so sánh mean median
        if mean > median:
            text += "Mean lớn hơn median → dữ liệu **lệch phải**, có một số giá trị lớn bất thường.\n\n"

        elif mean < median:
            text += "Mean nhỏ hơn median → dữ liệu **lệch trái**, có một số giá trị nhỏ bất thường.\n\n"

        else:
            text += "Mean gần bằng median → dữ liệu **phân bố khá cân bằng**.\n\n"

        # giải thích std
        if std < mean * 0.2:
            text += "Độ lệch chuẩn nhỏ → dữ liệu khá ổn định.\n\n"
        elif std < mean * 0.5:
            text += "Độ lệch chuẩn trung bình → dữ liệu có biến động vừa phải.\n\n"
        else:
            text += "Độ lệch chuẩn lớn → dữ liệu phân tán mạnh giữa các khách hàng.\n\n"

        explanations.append(text)

    return explanations


# ================= PASSWORD VALIDATION =================


def validate_password(pw):

    if len(pw) < 4:
        return False, "Password phải ít nhất 4 ký tự"

    if not re.search("[a-zA-Z]", pw):
        return False, "Password phải có chữ"

    if not re.search("[0-9]", pw):
        return False, "Password phải có số"

    return True, ""


# ================= SESSION =================

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = ""


# ================= LOGIN SUCCESS =================

if st.session_state.login:

    st.sidebar.success(f"Xin chào {st.session_state.user}")

    menu = [
        "Trang chủ",
        "Đổi username",
        "Đổi password",
        "Dashboard",
        "Logout",
    ]

    choice = st.sidebar.selectbox("Menu", menu)

    # ================= HOME =================
    if choice == "Trang chủ":

        st.markdown(
            """
        <style>

        .hero{
            padding:50px;
            border-radius:25px;
            background:linear-gradient(135deg,#1f4e79,#4fa3ff);
            text-align:center;
            color:white;
            box-shadow:0px 15px 40px rgba(0,0,0,0.25);
        }

        .hero-title{
            font-size:64px;
            font-weight:900;
        }

        .hero-subtitle{
            font-size:24px;
            opacity:0.9;
        }

        .feature-card{
            height:260px;
            padding:25px;
            border-radius:18px;
            background:white;
            box-shadow:0px 6px 25px rgba(0,0,0,0.1);

            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;

            text-align:center;
        }

        .feature-card:hover{
            transform:translateY(-6px);
            transition:0.3s;
            box-shadow:0px 12px 35px rgba(0,0,0,0.18);
        }

        .footer{
            text-align:center;
            color:gray;
            font-size:14px;
        }

        </style>
        """,
            unsafe_allow_html=True,
        )

        # ================= HERO =================

        st.markdown(
            """
        <div class="hero">

        <div class="hero-title">
        🏦 ATBank AI Customer Analytics
        </div>

        <div class="hero-subtitle">
        AI-powered banking analytics and customer churn prediction platform
        </div>

        </div>
        """,
            unsafe_allow_html=True,
        )

        st.write("")
        st.write("")

        # ================= KPI =================

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Customers Supported", "10,000+")
        col2.metric("AI Model Accuracy", "92%")
        col3.metric("Real-time Prediction", "Yes")
        col4.metric("System Version", "1.0")

        st.write("")
        st.write("")

        # ================= DASHBOARD PREVIEW =================

        st.subheader("📊 Analytics Dashboard Preview")

        st.image(
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71", width="stretch"
        )

        st.write("")
        st.write("")

        # ================= FEATURES =================

        st.subheader("🚀 Platform Features")

        f1, f2, f3 = st.columns(3)

        with f1:
            st.markdown(
                """
            <div class="feature-card">
            <h3>📊 Data Analytics</h3>
            <p>Automatic analysis of customer datasets.</p>
            <p>Statistics, distributions and correlation insights.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with f2:
            st.markdown(
                """
            <div class="feature-card">
            <h3>🧠 AI Prediction</h3>
            <p>Predict customer churn probability.</p>
            <p>Powered by RandomForest Machine Learning model.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with f3:
            st.markdown(
                """
            <div class="feature-card">
            <h3>👥 Customer Segmentation</h3>
            <p>Cluster customers using KMeans.</p>
            <p>Discover hidden business insights.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.write("")
        st.write("")

        # ================= WORKFLOW =================

        st.subheader("⚙️ System Workflow")

        st.markdown(
            """
        **1️⃣ Upload Dataset**  
        Upload customer dataset in CSV format.

        **2️⃣ AI Data Analysis**  
        Automatic statistics and data quality analysis.

        **3️⃣ Visualization Dashboard**  
        Interactive charts and correlation analysis.

        **4️⃣ Customer Segmentation**  
        Identify customer groups using clustering.

        **5️⃣ Churn Prediction**  
        Detect customers likely to leave the bank.

        **6️⃣ Export Results**  
        Download analysis report and predictions.
        """
        )

        st.write("")
        st.write("")

        # ================= FOOTER =================

        st.markdown(
            """
        <div class="footer">
        ATBank AI Customer Analytics Platform © 2026
        </div>
        """,
            unsafe_allow_html=True,
        )
    # ================= CHANGE USERNAME =================

    elif choice == "Đổi username":

        st.title("Đổi Username")

        new_user = st.text_input("Username mới")

        if st.button("Update"):

            db.update_username(st.session_state.user, new_user)

            st.session_state.user = new_user

            st.success("Đổi username thành công")

    # ================= CHANGE PASSWORD =================

    elif choice == "Đổi password":

        st.title("Đổi Password")

        new_pw = st.text_input("Password mới", type="password")
        confirm_pw = st.text_input("Confirm Password", type="password")

        if st.button("Update"):

            valid, msg = validate_password(new_pw)

            if not valid:
                st.error(msg)

            elif new_pw != confirm_pw:
                st.error("Password không khớp")

            else:

                db.update_password(st.session_state.user, new_pw)

                st.success("Đổi password thành công")

    # ================= DASHBOARD =================

    elif choice == "Dashboard":

        st.title("🏦 ATBank Customer Data Analytics & Churn Prediction")

        file = st.file_uploader("Upload Customer Dataset (CSV)", type="csv")

        if file:

            df = pd.read_csv(file)

            st.header("🤖 AI Data Analysis Report")

            if st.button("Generate AI Report"):

                with st.spinner("AI đang phân tích dataset..."):

                    report = ai_generate_report(df)

                st.success("Report generated")

                st.markdown(report)

            # ================= DATASET OVERVIEW =================

            st.header("📊 Dataset Overview")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Rows", df.shape[0])
            col2.metric("Columns", df.shape[1])
            col3.metric("Missing Values", df.isnull().sum().sum())
            col4.metric("Duplicate Rows", df.duplicated().sum())

            st.dataframe(df.head())

            # ================= DATA TYPES =================

            st.subheader("Data Types")

            dtype_df = pd.DataFrame(
                {"Column": df.columns, "Type": df.dtypes.astype(str)}
            )

            st.dataframe(dtype_df)

            # ================= STATISTICAL SUMMARY =================

            st.header("📈 Statistical Summary")

            st.dataframe(df.describe())
            st.header("📊 Statistical Interpretation")

            explanations = explain_statistics(df)

            for e in explanations:
                st.markdown(e)

            # ================= MISSING VALUES =================

            st.header("⚠ Missing Values Analysis")

            missing = df.isnull().sum()

            missing_df = pd.DataFrame(
                {"Column": missing.index, "Missing": missing.values}
            )

            fig_missing = px.bar(
                missing_df, x="Column", y="Missing", title="Missing Values per Column"
            )

            st.plotly_chart(fig_missing)

            # ================= NUMERIC DATA =================

            numeric = df.select_dtypes(include=np.number)

            if len(numeric.columns) > 0:

                # Distribution

                st.header("📊 Feature Distribution")

                feature = st.selectbox("Select Feature", numeric.columns)

                fig = px.histogram(df, x=feature)

                st.plotly_chart(fig)

                # Boxplot

                st.header("📦 Outlier Detection")

                fig_box = px.box(df, y=feature)

                st.plotly_chart(fig_box)

                # Correlation

                st.header("🔥 Correlation Heatmap")

                corr = numeric.corr()

                fig_corr, ax = plt.subplots(figsize=(10, 6))

                sns.heatmap(corr, cmap="coolwarm", annot=True, ax=ax)

                st.pyplot(fig_corr)

            # ================= CUSTOMER SEGMENTATION =================

            st.header("👥 Customer Segmentation")

            if len(numeric.columns) >= 2:

                kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

                df["Cluster"] = kmeans.fit_predict(numeric)

                fig_cluster = px.scatter(
                    df, x=numeric.columns[0], y=numeric.columns[1], color="Cluster"
                )

                st.plotly_chart(fig_cluster)

            # ================= PREDICTION =================

            st.header("🧠 Churn Prediction")

            try:

                session = ort.InferenceSession(MODEL_PATH)

                input_name = session.get_inputs()[0].name
                expected = session.get_inputs()[0].shape[1]

                df_model = df.drop(
                    columns=["RowNumber", "CustomerId", "Surname"], errors="ignore"
                )

                X = df_model.select_dtypes(include=np.number)

                if X.shape[1] > expected:
                    X = X.iloc[:, :expected]

                if X.shape[1] < expected:

                    st.error(
                        f"Dataset có {X.shape[1]} features nhưng model cần {expected}"
                    )

                    st.stop()

                X = X.values.astype(np.float32)

                pred = session.run(None, {input_name: X})[0]

                if len(pred.shape) > 1:
                    pred = pred[:, 1]

                df["Churn Probability"] = pred

                df["Risk Level"] = df["Churn Probability"].apply(
                    lambda x: (
                        "High Risk"
                        if x > 0.7
                        else "Medium Risk" if x > 0.4 else "Low Risk"
                    )
                )

                st.dataframe(df)

            except Exception as e:

                st.error("Prediction Error")
                st.code(str(e))

            # ================= RISK DISTRIBUTION =================

            if "Risk Level" in df.columns:

                st.header("⚠ Customer Risk Distribution")

                fig_risk = px.pie(df, names="Risk Level")

                st.plotly_chart(fig_risk)

            # ================= TOP RISK =================

            if "Churn Probability" in df.columns:

                st.header("🚨 Top 10 Risk Customers")

                top_risk = df.sort_values("Churn Probability", ascending=False).head(10)

                st.dataframe(top_risk)

            # ================= AUTO INSIGHT =================

            st.header("🧠 Automatic Data Insights")

            insights = []

            for col in numeric.columns:

                mean = numeric[col].mean()
                std = numeric[col].std()

                outliers = numeric[numeric[col] > mean + 2 * std]

                if len(outliers) > 0:

                    insights.append(f"{col} có {len(outliers)} giá trị cao bất thường")

                if mean > numeric[col].median():

                    insights.append(f"{col} có xu hướng lệch phải")

            if insights:

                for i in insights:
                    st.write("•", i)

            else:

                st.write("Dataset khá cân bằng")

            # ================= DOWNLOAD =================

            csv = df.to_csv(index=False)

            st.download_button(
                "Download Analysis Result", csv, "analysis_result.csv", "text/csv"
            )

    # ================= LOGOUT =================

    elif choice == "Logout":

        st.session_state.login = False
        st.session_state.user = ""

        st.rerun()


# ================= LOGIN PAGE =================

else:

    menu = ["Login", "Register", "Forgot Password"]

    choice = st.sidebar.selectbox("Menu", menu, index=menu.index(st.session_state.page))

    st.session_state.page = choice

    if choice == "Login":

        st.title("Login")

        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")

        if st.button("Login"):

            res = db.login(user, pw)

            if res:

                st.session_state.login = True
                st.session_state.user = user

                st.rerun()

            else:

                st.error("Sai username hoặc password")

    elif choice == "Register":

        st.title("Register")

        user = st.text_input("Username")
        email = st.text_input("Email")
        pw = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")

        if st.button("Register"):

            user = user.strip()
            email = email.lower().strip()

            if not user or not email or not pw or not confirm:
                st.error("Vui lòng nhập đầy đủ thông tin")

            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("Email không hợp lệ")

            elif pw != confirm:
                st.error("Password không khớp")

            else:
                valid, msg = validate_password(pw)

                if not valid:
                    st.error(msg)

                elif db.email_exists(email):
                    st.error("Email đã tồn tại")

                else:
                    db.add_user(user, pw, email)

                    st.success("Đăng ký thành công")

                    st.session_state.page = "Login"
                    st.rerun()

    elif choice == "Forgot Password":

        st.title("Reset Password")

        if st.session_state.reset_step == 1:

            email = st.text_input("Nhập email")

            if st.button("Send OTP"):

                if not db.email_exists(email):
                    st.error("Email chưa đăng ký")

                else:
                    user = db.get_username_by_email(email)

                    code = str(np.random.randint(100000, 999999))

                    db.save_reset_code(user, code)

                    send_email(
                        email,
                        "ATBank - Reset Password",
                        f"Mã OTP của bạn là: {code}",
                    )

                    st.session_state.reset_user = user
                    st.session_state.reset_step = 2

                    st.success("Đã gửi OTP qua email")
                    st.rerun()

        elif st.session_state.reset_step == 2:

            code = st.text_input("Nhập OTP")
            new_pw = st.text_input("Password mới", type="password")

            if st.button("Reset Password"):

                user = st.session_state.reset_user

                if not db.check_reset_code(user, code):
                    st.error("OTP không đúng")

                else:
                    db.update_password(user, new_pw)
                    db.clear_reset_code(user)

                    st.success("Đổi password thành công")

                    st.session_state.reset_step = 1
                    st.session_state.page = "Login"

                    st.rerun()

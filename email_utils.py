import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Lấy email/password
try:
    # Streamlit Cloud
    EMAIL_ADDRESS = st.secrets["email"]["address"]
    EMAIL_PASSWORD = st.secrets["email"]["password"]
except Exception:
    # Local
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(to, subject, content):

    msg = MIMEText(content)

    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            server.sendmail(EMAIL_ADDRESS, to, msg.as_string())

        print("Email sent successfully")

    except Exception as e:

        print("Email error:", e)

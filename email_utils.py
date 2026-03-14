import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Lấy email/password
try:
    # Streamlit Cloud
    GMAIL_USER = st.secrets["email"]["address"]
    GMAIL_PASS = st.secrets["email"]["password"]
except Exception:
    # Local
    GMAIL_USER = os.getenv("EMAIL_ADDRESS")
    GMAIL_PASS = os.getenv("EMAIL_PASSWORD")


def send_email(to, subject, content):

    msg = MIMEText(content)

    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = to

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

            server.login(GMAIL_USER, GMAIL_PASS)

            server.sendmail(GMAIL_USER, to, msg.as_string())

        print("Email sent successfully")

    except Exception as e:

        print("Email error:", e)

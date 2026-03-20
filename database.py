# database.py
import sqlite3
import hashlib
import os
from pathlib import Path


DB_PATH = os.getenv("DB_PATH", "data/data.db")
Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)


def get_conn():
    """Trả về connection tới SQLite DB"""
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def execute_query(query, params=(), fetchone=False, commit=False):
    """Hàm tiện lợi chạy query"""
    conn = get_conn()
    c = conn.cursor()
    c.execute(query, params)
    result = c.fetchone() if fetchone else c.fetchall()
    if commit:
        conn.commit()
    conn.close()
    return result


def hash_password(pw):
    """Hash password bằng SHA256"""
    return hashlib.sha256(pw.encode()).hexdigest()


# ================= INIT =================
def create_tables():
    """Tạo bảng users và reset_codes nếu chưa tồn tại"""
    execute_query(
        """
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT,
            email TEXT UNIQUE
        )
    """,
        commit=True,
    )

    execute_query(
        """
        CREATE TABLE IF NOT EXISTS reset_codes(
            username TEXT,
            code TEXT
        )
    """,
        commit=True,
    )


# ================= REGISTER =================
def add_user(username, password, email):
    """Thêm user mới"""
    try:
        execute_query(
            "INSERT INTO users(username, password, email) VALUES (?, ?, ?)",
            (username, hash_password(password), email),
            commit=True,
        )
        return True
    except Exception as e:
        print("Add user error:", e)
        return False


# ================= LOGIN =================
def login(username, password):
    res = execute_query(
        "SELECT password FROM users WHERE username=?", (username,), fetchone=True
    )
    return res and res[0] == hash_password(password)


# ================= CHECK =================
def email_exists(email):
    res = execute_query("SELECT 1 FROM users WHERE email=?", (email,), fetchone=True)
    return res is not None


def username_exists(username):
    res = execute_query(
        "SELECT 1 FROM users WHERE username=?", (username,), fetchone=True
    )
    return res is not None


def get_username_by_email(email):
    res = execute_query(
        "SELECT username FROM users WHERE email=?", (email,), fetchone=True
    )
    return res[0] if res else None


# ================= UPDATE =================
def update_password(username, new_pw):
    execute_query(
        "UPDATE users SET password=? WHERE username=?",
        (hash_password(new_pw), username),
        commit=True,
    )


def update_username(old, new):
    if username_exists(new):
        return False
    execute_query(
        "UPDATE users SET username=? WHERE username=?", (new, old), commit=True
    )
    return True


# ================= RESET OTP =================
def save_reset_code(username, code):
    execute_query("DELETE FROM reset_codes WHERE username=?", (username,), commit=True)
    execute_query(
        "INSERT INTO reset_codes(username, code) VALUES (?, ?)",
        (username, code),
        commit=True,
    )


def check_reset_code(username, code):
    res = execute_query(
        "SELECT 1 FROM reset_codes WHERE username=? AND code=?",
        (username, code),
        fetchone=True,
    )
    return res is not None


def clear_reset_code(username):
    execute_query("DELETE FROM reset_codes WHERE username=?", (username,), commit=True)


# ================= INIT DB KHI IMPORT =================
create_tables()

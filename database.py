import sqlite3
import hashlib

DB_PATH = "data.db"


# ================= CONNECT =================
def get_conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# ================= INIT TABLE =================
def create_tables():
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        """
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    """
    )

    conn.commit()
    conn.close()


# ================= HASH PASSWORD =================
def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()


# ================= REGISTER =================
def add_user(username, password, email):
    try:
        conn = get_conn()
        c = conn.cursor()

        c.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, hash_password(password), email),
        )

        conn.commit()
        conn.close()
        return True

    except:
        return False


# ================= LOGIN =================
def login(username, password):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "SELECT password FROM users WHERE username=?",
        (username,),
    )

    res = c.fetchone()
    conn.close()

    if res and res[0] == hash_password(password):
        return True

    return False


# ================= CHECK EXIST =================
def email_exists(email):
    conn = get_conn()
    c = conn.cursor()

    c.execute("SELECT 1 FROM users WHERE email=?", (email,))
    res = c.fetchone()

    conn.close()
    return res is not None


def username_exists(username):
    conn = get_conn()
    c = conn.cursor()

    c.execute("SELECT 1 FROM users WHERE username=?", (username,))
    res = c.fetchone()

    conn.close()
    return res is not None


# ================= GET USER =================
def get_username_by_email(email):
    conn = get_conn()
    c = conn.cursor()

    c.execute("SELECT username FROM users WHERE email=?", (email,))
    res = c.fetchone()

    conn.close()
    return res[0] if res else None


# ================= UPDATE =================
def update_password(username, new_pw):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "UPDATE users SET password=? WHERE username=?",
        (hash_password(new_pw), username),
    )

    conn.commit()
    conn.close()


def update_password_by_email(email, new_pw):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "UPDATE users SET password=? WHERE email=?",
        (hash_password(new_pw), email),
    )

    conn.commit()
    conn.close()


def update_username(old, new):
    if username_exists(new):
        return False

    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "UPDATE users SET username=? WHERE username=?",
        (new, old),
    )

    conn.commit()
    conn.close()
    return True

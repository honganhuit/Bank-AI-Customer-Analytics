import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()


def create_tables():

    c.execute(
        """
    CREATE TABLE IF NOT EXISTS users(
        username TEXT UNIQUE,
        password TEXT,
        email TEXT UNIQUE,
        verify_code TEXT,
        is_verified INTEGER DEFAULT 0
    )
    """
    )

    c.execute(
        """
    CREATE TABLE IF NOT EXISTS reset_tokens(
        email TEXT,
        token TEXT
    )
    """
    )

    conn.commit()


# ================= REGISTER =================


def add_user(username, password, email, code):

    c.execute(
        "INSERT INTO users(username,password,email,verify_code,is_verified) VALUES(?,?,?,?,0)",
        (username, password, email, code),
    )

    conn.commit()


# ================= VERIFY =================


def verify_user(code):

    c.execute("UPDATE users SET is_verified=1 WHERE verify_code=?", (code,))

    conn.commit()


# ================= LOGIN =================


def login(username, password):

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=? AND is_verified=1",
        (username, password),
    )

    return c.fetchone()


# ================= CHECK =================


def email_exists(email):

    c.execute("SELECT email FROM users WHERE email=?", (email,))
    return c.fetchone()


def username_exists(username):

    c.execute("SELECT username FROM users WHERE username=?", (username,))
    return c.fetchone()


# ================= UPDATE =================


def update_password(username, new_pw):

    c.execute("UPDATE users SET password=? WHERE username=?", (new_pw, username))

    conn.commit()


def update_password_by_email(email, new_pw):

    c.execute("UPDATE users SET password=? WHERE email=?", (new_pw, email))

    conn.commit()


def update_username(old_username, new_username):

    c.execute(
        "UPDATE users SET username=? WHERE username=?", (new_username, old_username)
    )

    conn.commit()


# ================= RESET PASSWORD =================


def save_reset_token(email, token):

    c.execute("DELETE FROM reset_tokens WHERE email=?", (email,))

    c.execute("INSERT INTO reset_tokens(email, token) VALUES (?, ?)", (email, token))

    conn.commit()


def get_email_by_token(token):

    print("Token tìm:", token)

    c.execute("SELECT email FROM reset_tokens WHERE token=?", (str(token),))

    result = c.fetchone()

    print("Kết quả query:", result)

    if result:
        return result[0]

    return None


def delete_token(token):

    c.execute("DELETE FROM reset_tokens WHERE token=?", (token,))

    conn.commit()

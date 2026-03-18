# database.py  — place in backend/ folder
import pymysql
import os

def get_connection():
    return pymysql.connect(
        host     = os.environ.get('MYSQLHOST',     'localhost'),
        port     = int(os.environ.get('MYSQLPORT', 3306)),
        user     = os.environ.get('MYSQLUSER',     'root'),
        password = os.environ.get('MYSQLPASSWORD', ''),
        database = os.environ.get('MYSQLDATABASE', 'railway'),
        cursorclass = pymysql.cursors.DictCursor
    )

def init_db():
    """Create all tables if they don't exist."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS groups_table (
                    group_id   VARCHAR(50)  PRIMARY KEY,
                    name       VARCHAR(100) NOT NULL,
                    created_by VARCHAR(50),
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS members (
                    id       INT AUTO_INCREMENT PRIMARY KEY,
                    group_id VARCHAR(50)  NOT NULL,
                    name     VARCHAR(100) NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS votes (
                    id           INT AUTO_INCREMENT PRIMARY KEY,
                    group_id     VARCHAR(50)  NOT NULL,
                    user_name    VARCHAR(100) NOT NULL,
                    preferences  JSON         NOT NULL,
                    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id    VARCHAR(20)  PRIMARY KEY,
                    name       VARCHAR(100) NOT NULL,
                    email      VARCHAR(100) UNIQUE NOT NULL,
                    phone      VARCHAR(20),
                    dob        VARCHAR(20),
                    password   VARCHAR(64)  NOT NULL,
                    token      VARCHAR(50),
                    travel_preferences JSON,
                    `groups`   JSON,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id          VARCHAR(50)  PRIMARY KEY,
                    group_id    VARCHAR(50)  NOT NULL,
                    paid_by     VARCHAR(100) NOT NULL,
                    amount      FLOAT        NOT NULL,
                    description VARCHAR(255),
                    category    VARCHAR(50),
                    split_among JSON,
                    splits      JSON,
                    split_type  VARCHAR(20),
                    date        VARCHAR(20),
                    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id           VARCHAR(50)  PRIMARY KEY,
                    group_id     VARCHAR(50)  NOT NULL,
                    title        VARCHAR(255) NOT NULL,
                    description  TEXT,
                    category     VARCHAR(50),
                    assigned_to  VARCHAR(100),
                    priority     VARCHAR(20),
                    due_date     VARCHAR(20),
                    completed    BOOLEAN DEFAULT FALSE,
                    completed_at DATETIME,
                    created_at   DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

        conn.commit()
        print("✅ Database tables ready")
    finally:
        conn.close()

# # database.py  — place in backend/ folder
# import pymysql
# import os

# def get_connection():
#     return pymysql.connect(
#         host     = os.environ.get('MYSQLHOST',     'localhost'),
#         port     = int(os.environ.get('MYSQLPORT', 3306)),
#         user     = os.environ.get('MYSQLUSER',     'root'),
#         password = os.environ.get('MYSQLPASSWORD', ''),
#         database = os.environ.get('MYSQLDATABASE', 'railway'),
#         cursorclass = pymysql.cursors.DictCursor
#     )

# def init_db():
#     """Create all tables if they don't exist."""
#     conn = get_connection()
#     try:
#         with conn.cursor() as cur:

#             cur.execute("""
#                 CREATE TABLE IF NOT EXISTS groups_table (
#                     group_id   VARCHAR(50)  PRIMARY KEY,
#                     name       VARCHAR(100) NOT NULL,
#                     created_by VARCHAR(50),
#                     created_at DATETIME DEFAULT CURRENT_TIMESTAMP
#                 )
#             """)

#             cur.execute("""
#                 CREATE TABLE IF NOT EXISTS members (
#                     id       INT AUTO_INCREMENT PRIMARY KEY,
#                     group_id VARCHAR(50)  NOT NULL,
#                     name     VARCHAR(100) NOT NULL
#                 )
#             """)

#             cur.execute("""
#                 CREATE TABLE IF NOT EXISTS votes (
#                     id           INT AUTO_INCREMENT PRIMARY KEY,
#                     group_id     VARCHAR(50)  NOT NULL,
#                     user_name    VARCHAR(100) NOT NULL,
#                     preferences  JSON         NOT NULL,
#                     submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
#                 )
#             """)

#             cur.execute("""
#                 CREATE TABLE IF NOT EXISTS users (
#                     user_id    VARCHAR(20)  PRIMARY KEY,
#                     name       VARCHAR(100) NOT NULL,
#                     email      VARCHAR(100) UNIQUE NOT NULL,
#                     phone      VARCHAR(20),
#                     dob        VARCHAR(20),
#                     password   VARCHAR(64)  NOT NULL,
#                     token      VARCHAR(50),
#                     travel_preferences JSON,
#                     `groups`   JSON,
#                     created_at DATETIME DEFAULT CURRENT_TIMESTAMP
#                 )
#             """)

#             cur.execute("""
#                 CREATE TABLE IF NOT EXISTS expenses (
#                     id          VARCHAR(50)  PRIMARY KEY,
#                     group_id    VARCHAR(50)  NOT NULL,
#                     paid_by     VARCHAR(100) NOT NULL,
#                     amount      FLOAT        NOT NULL,
#                     description VARCHAR(255),
#                     category    VARCHAR(50),
#                     split_among JSON,
#                     splits      JSON,
#                     split_type  VARCHAR(20),
#                     date        VARCHAR(20),
#                     created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
#                 )
#             """)

#             cur.execute("""
#                 CREATE TABLE IF NOT EXISTS tasks (
#                     id           VARCHAR(50)  PRIMARY KEY,
#                     group_id     VARCHAR(50)  NOT NULL,
#                     title        VARCHAR(255) NOT NULL,
#                     description  TEXT,
#                     category     VARCHAR(50),
#                     assigned_to  VARCHAR(100),
#                     priority     VARCHAR(20),
#                     due_date     VARCHAR(20),
#                     completed    BOOLEAN DEFAULT FALSE,
#                     completed_at DATETIME,
#                     created_at   DATETIME DEFAULT CURRENT_TIMESTAMP
#                 )
#             """)

#         conn.commit()
#         print("✅ Database tables ready")
#     finally:
#         conn.close()

import mysql.connector
from mysql.connector import Error

# ── Railway MySQL Configuration ───────────────────────────────────────────
DB_CONFIG = {
    'host':     'yamanote.proxy.rlwy.net',
    'port':     42026,
    'user':     'root',
    'password': 'UabDqCNWfHtHHLfvyTrnLCPLEczZMRWX',
    'database': 'railway',
    'autocommit': True,
    'connection_timeout': 30
}

def get_connection():
    """Get a database connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        return None

def init_db():
    """Create all tables if they don't exist."""
    conn = get_connection()
    if not conn:
        print("❌ Could not connect to database!")
        return False
    cursor = conn.cursor()
    try:
        # ── Users ─────────────────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id      VARCHAR(8)   PRIMARY KEY,
                name         VARCHAR(100) NOT NULL,
                email        VARCHAR(150) UNIQUE NOT NULL,
                phone        VARCHAR(15)  UNIQUE NOT NULL,
                dob          VARCHAR(20)  NOT NULL,
                password     VARCHAR(64)  NOT NULL,
                token        VARCHAR(36),
                created_at   DATETIME     DEFAULT NOW()
            )
        """)

        # ── User preferences ──────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_preferences (
                id           INT          PRIMARY KEY AUTO_INCREMENT,
                user_id      VARCHAR(8)   NOT NULL,
                budget       VARCHAR(10)  DEFAULT 'medium',
                trip_duration INT         DEFAULT 7,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
        """)

        # ── User travel styles ────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_travel_styles (
                id           INT          PRIMARY KEY AUTO_INCREMENT,
                user_id      VARCHAR(8)   NOT NULL,
                style        VARCHAR(50)  NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
        """)

        # ── User favourite destinations ───────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_fav_destinations (
                id           INT          PRIMARY KEY AUTO_INCREMENT,
                user_id      VARCHAR(8)   NOT NULL,
                destination  VARCHAR(100) NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
        """)

        # ── Groups ────────────────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups_table (
                group_id     VARCHAR(30)  PRIMARY KEY,
                name         VARCHAR(100) NOT NULL,
                created_by   VARCHAR(8),
                created_at   DATETIME     DEFAULT NOW()
            )
        """)

        # ── Group members ─────────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS group_members (
                id           INT          PRIMARY KEY AUTO_INCREMENT,
                group_id     VARCHAR(30)  NOT NULL,
                member_name  VARCHAR(100) NOT NULL,
                joined_at    DATETIME     DEFAULT NOW(),
                FOREIGN KEY (group_id) REFERENCES groups_table(group_id) ON DELETE CASCADE
            )
        """)

        # ── Votes ─────────────────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS votes (
                id           INT          PRIMARY KEY AUTO_INCREMENT,
                group_id     VARCHAR(30)  NOT NULL,
                user_name    VARCHAR(100) NOT NULL,
                destinations TEXT,
                budget       VARCHAR(10),
                travel_style TEXT,
                duration     INT          DEFAULT 7,
                month        VARCHAR(20),
                submitted_at DATETIME     DEFAULT NOW(),
                FOREIGN KEY (group_id) REFERENCES groups_table(group_id) ON DELETE CASCADE
            )
        """)

        # ── Itineraries ───────────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS itineraries (
                id           INT          PRIMARY KEY AUTO_INCREMENT,
                group_id     VARCHAR(30)  NOT NULL,
                destination  VARCHAR(100),
                duration     INT,
                budget       VARCHAR(10),
                month        VARCHAR(20),
                days_data    LONGTEXT,
                cost_data    TEXT,
                weather_data TEXT,
                generated_at DATETIME     DEFAULT NOW(),
                FOREIGN KEY (group_id) REFERENCES groups_table(group_id) ON DELETE CASCADE
            )
        """)

        # ── Expenses ──────────────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                expense_id   VARCHAR(30)  PRIMARY KEY,
                group_id     VARCHAR(30)  NOT NULL,
                paid_by      VARCHAR(100) NOT NULL,
                amount       DECIMAL(10,2) NOT NULL,
                description  VARCHAR(200) NOT NULL,
                category     VARCHAR(20)  DEFAULT 'other',
                split_among  TEXT,
                splits       TEXT,
                split_type   VARCHAR(10)  DEFAULT 'equal',
                expense_date DATE,
                created_at   DATETIME     DEFAULT NOW(),
                FOREIGN KEY (group_id) REFERENCES groups_table(group_id) ON DELETE CASCADE
            )
        """)

        # ── Tasks ─────────────────────────────────────────────────────
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                task_id      VARCHAR(30)  PRIMARY KEY,
                group_id     VARCHAR(30)  NOT NULL,
                title        VARCHAR(200) NOT NULL,
                description  TEXT,
                category     VARCHAR(20)  DEFAULT 'other',
                assigned_to  VARCHAR(100) DEFAULT 'Unassigned',
                priority     VARCHAR(10)  DEFAULT 'medium',
                due_date     DATE,
                completed    BOOLEAN      DEFAULT FALSE,
                completed_at DATETIME,
                created_at   DATETIME     DEFAULT NOW(),
                FOREIGN KEY (group_id) REFERENCES groups_table(group_id) ON DELETE CASCADE
            )
        """)

        print("✅ All tables created successfully!")
        return True

    except Error as e:
        print(f"❌ Error creating tables: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def execute_query(query, params=None, fetch=False):
    """Execute a query and optionally fetch results."""
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Query error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def execute_one(query, params=None):
    """Execute a query and fetch one result."""
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        return cursor.fetchone()
    except Error as e:
        print(f"Query error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    print("🔌 Connecting to Railway MySQL...")
    if init_db():
        print("🎉 Database ready!")
    else:
        print("❌ Database setup failed!")



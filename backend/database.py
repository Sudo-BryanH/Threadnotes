import psycopg


def get_login(conn, email):
    
    with conn.cursor() as cur:
        cur.execute("""
            SELECT email, password
            FROM users
            WHERE email = {email}
            """)
        return cur[0]
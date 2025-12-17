from contextlib import contextmanager
import psycopg2
from src.database.config import config

@contextmanager
def db_connection(section='postgresql'):
    """Connection manager for the database"""
    conn = None
    try:
        prams= config(section=section) #read sittings
        conn = psycopg2.connect(**prams) #create connecti
        conn.autocommit = False # تعطيل الـ auto-commit
        print("Connected to PostgreSQL")
        yield conn # as return ⏸️ إرجاع الاتصال وتوقف مؤقت

        # 🔹 الكود هنا سينفذ فقط إذا لم يكن هناك أخطاء
        # conn.commit()  # لو أردنا عمل commit تلقائي


    except psycopg2.DatabaseError as e:
        if conn:
            conn.rollback() # التراجع عن التغييرات
        print("Error while connecting to PostgreSQL", e)
    finally:
        if conn:
            conn.close()
            print("Connection to PostgreSQL closed")


def test_connection(section='postgresql'):
    """Testing connection to PostgreSQL database"""
    try:
        with db_connection(section) as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT version()')
                version_info = cursor.fetchone()[0]

                cursor.execute('SELECT current_database(), current_user()')
                db_info = cursor.fetchone()
                print("Results of the current database is: ")
                print(f"Database version: {version_info.split(',')}")
                print(f"Database: {db_info[0]}")
                print(f"Database current user: {db_info[1]}")
                return True
    except Exception as e:
        print("Error while connecting to PostgreSQL", e)
        return False







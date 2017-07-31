import psycopg2

from plugs_status.settings import app_settings as settings

def check_connection():
    if settings['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
        try:
            conn = psycopg2.connect(
                dbname="{0}".format(settings['NAME']),
                user="{0}".format(settings['USER']),
                password="{0}".format(settings['PASSWORD']),
                host="{0}".format(settings['HOST']),
                port="{0}".format(settings['PORT']),
                connect_timeout=3
            )
            cur = conn.cursor()
            cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            cur.fetchone()
        except psycopg2.DatabaseError:
            return False
        cur.close()
        conn.close()
    return True

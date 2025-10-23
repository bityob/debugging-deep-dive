import os

def main(event, context):
    from remote_pdb import RemotePdb
    RemotePdb("0.tcp.eu.ngrok.io", 13395, reverse=True).set_trace()

    import psycopg

    conn = psycopg.connect(
        host=os.environ["PG_HOST"],
        dbname=os.environ["PG_DB"],
        user=os.environ["PG_USER"],
        password=os.environ["PG_PASSWORD"],
        port=os.environ["PG_PORT"],
    )
    with conn.cursor() as cur:
        cur.execute("SELECT now();")
        now = cur.fetchone()
    conn.close()

    return {"statusCode": 200, "body": f"PostgreSQL time: {now[0]}"}

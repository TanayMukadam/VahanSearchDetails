import pymysql
import json

def connection():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="Tanay@82629",
            database="vahan_search"
        )
        print("--> DataBase Connected Successfully")
        return connection
    except Exception as e:
        print(f"Database Connection Failed: {e}")
        return None


db_conn = connection()
if db_conn:
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)

    query = """
    SELECT * FROM vehicle_details WHERE regNo = "DL10AC1234"
    """
    cursor.execute(query)
    results = cursor.fetchall()   # list of dicts

    # Save results into JSON file (overwrite file with latest result)
    with open("data.json", "w") as file:
        json.dump(results, file, indent=4)

    print("--> Data saved to data.json")

    cursor.close()
    db_conn.close()

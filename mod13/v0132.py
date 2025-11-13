from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        port=3306,
        user="testi",
        database="flight_game",
        host="localhost",
        password="salasana",
        autocommit=True
    )
    return connection


@app.route('/kenttä/<string:icao>', methods=['GET'])
def get_icao_code(icao):
    """Palauttaa lentokentän nimen ICAO-koodin perusteella."""
    connection = get_db_connection()
    cursor = connection.cursor()

    # Prepare the SQL query
    sql = f"SELECT name FROM airport WHERE ident = '{icao}'"
    cursor.execute(sql)

    # Fetch the result
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        response = {
            "ICAO": icao,
            "Name": result[0]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt."}), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)



import mysql.connector
connection = mysql.connector.connect (
    port=3306,
    user="testi",
    database="flight_game",
    host="localhost",
    password="salasana",
    autocommit=True)
cursor = connection.cursor()
def get_icao_code (code):
    sql = f"SELECT name FROM airport WHERE ident = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if not result:
        return "Not found"
    return result[0]
ICAO_code = input("Anna ICAO koodi: ")
ICAO = get_icao_code(ICAO_code)
print(f"ICAO: {ICAO_code}, hakutulos: {ICAO}")

def get_country_airport(code):
    sql = f"SELECT type FROM airport WHERE iso_country = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"Koodi: {country_airport}")
    print(result)
    if not result:
        return "Not found"
    return result[0]
country_airport = input("Anna maan koodi: ")
country = get_country_airport(country_airport)

from geopy import distance
def get_icao_code2 (code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        return "Not found"
    return result[0]
ICAO_code2 = input("Anna ICAO koodi: ")
ICAO_CODE2 = input("Anna toinen ICAO koodi: ")
ICAO2 = get_icao_code2(ICAO_code2)
icao2 = get_icao_code2(ICAO_CODE2)
print(f"Ensimmäinen ICAO koodi: {ICAO2}, Toinen ICAO koodi: {icao2}")
from geopy import distance
print(distance.distance(ICAO2, icao2).km)

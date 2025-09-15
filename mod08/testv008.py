import mysql.connector
connection = mysql.connector.connect (
    port=3306,
    user="testi",
    database="flight_game",
    host="localhost",
    password="salasana",
    autocommit=True)

cursor = connection.cursor()
cursor.execute("select name, iso_country from country")
result = cursor.fetchone()
print(result)
result = cursor.fetchone()
print(result)
result = cursor.fetchmany(3)
print(result)
result = cursor.fetchall()
print(result)
print(f"Result listan pituus on: {len(result)}")
print(result[0] [1])
for country in result:
    print(f"Maan {country[0]} maakoodi on: {country[1]}")
def get_country_name_by_code(code):
    sql = f"SELECT name FROM country WHERE iso_country = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if not result:
        return "Not found"
    return result[0]
country_code = input("Anna maakoodi: ")
country = get_country_name_by_code(country_code)
print(f"Maakoodi: {country_code}, hakutulos: {country}")


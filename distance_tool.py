import sqlite3
import math

DB_NAME = "cities.db"


# --------------------------
# DATABASE SETUP
# --------------------------

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        name TEXT PRIMARY KEY,
        latitude REAL,
        longitude REAL
    )
    """)

    conn.commit()
    conn.close()


def get_city(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT latitude, longitude FROM cities WHERE name = ?", (name.lower(),))
    result = cursor.fetchone()

    conn.close()
    return result


def save_city(name, lat, lon):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR REPLACE INTO cities (name, latitude, longitude) VALUES (?, ?, ?)",
        (name.lower(), lat, lon)
    )

    conn.commit()
    conn.close()


# --------------------------
# HAVERSINE FORMULA
# --------------------------

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points on Earth (km)"""

    R = 6371  # Earth radius in km

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# --------------------------
# USER INPUT LOGIC
# --------------------------

def get_or_create_city(name):
    city = get_city(name)

    if city:
        print(f"{name} found in DB.")
        return city

    print(f"{name} not found. Please enter coordinates.")

    lat = float(input("Enter latitude: "))
    lon = float(input("Enter longitude: "))

    save_city(name, lat, lon)

    return lat, lon


# --------------------------
# MAIN PROGRAM
# --------------------------

def main():
    init_db()

    city1 = input("Enter first city: ")
    city2 = input("Enter second city: ")

    lat1, lon1 = get_or_create_city(city1)
    lat2, lon2 = get_or_create_city(city2)

    distance = calculate_distance(lat1, lon1, lat2, lon2)

    print(f"\nDistance between {city1} and {city2}: {round(distance, 2)} km")


if __name__ == "__main__":
    main()
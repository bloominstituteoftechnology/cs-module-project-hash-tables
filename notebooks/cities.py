"""
Read the CSV file
Build Various indexes
* what are all the city names in a particular state
Have a repl to query cities per state
"""
import csv

# Key: state name, value: list of cities in that state
cities_per_state = {}
states_per_city = {}


def read_csv_data():
    with open("cities.csv", newline=' ') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # list of cities + grab cities and  will place then in here:

            # if row['state_id'] not in cities_per_state:
            state_id = row['state_id']
            city = row['city']

            # Cities per state

            if state_id not in cities_per_state:
                # our empty list
                cities_per_state[state_id] = []
                cities_per_state[state_id].append(city)
                # print(row['city'], row[' state_id'])

            # States per city
            if city not in states_per_city:
                states_per_city[city] = []
            states_per_city[city].append(state_id)


def main():
    print("Reading...")

    read_csv_data()

    while True:
        """
        state_id = input("Enter a state: ").upper()
        print(cities_per_state[state_id])

        city = input("Enter a city: ")
        """

        city = input("Enter a city: ")
        print(states_per_city[city])
        # state_id = input("Enter a state: ").upper()

        # print(len(cities_per_state[state_id]))
        # print(cities_per_state[state_id])

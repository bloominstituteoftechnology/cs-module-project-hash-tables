"""
Read the CSV file
Build various indexes
* What are all the city names in a particular state
Have a repl to query cities per state
"""
import csv

cities_per_state = {}   # Key: state name, value: list of cities in that state
states_per_city = {}

population_buckets = {}


def read_csv_data():
    with open("cities.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            state_id = row['state_id']
            city = row['city']

            # Cities per state

            if state_id not in cities_per_state:
                cities_per_state[state_id] = []

            cities_per_state[state_id].append(city)

            # States per city

            if city not in states_per_city:
                states_per_city[city] = []

            states_per_city[city].append(state_id)

            # Population buckets

            population = int(float(row['population']))
            city_info = f'{city} {state_id} ({population})'

            if population < 10:
                population_buckets[10].append(city_info)
            elif population < 100:
                population_buckets[100].append(city_info)
            elif population < 1000:
                population_buckets[1000].append(city_info)
            elif population < 10000:
                population_buckets[10000].append(city_info)
            elif population < 100000:
                population_buckets[100000].append(city_info)
            elif population < 1000000:
                population_buckets[1000000].append(city_info)
            elif population < 10000000:
                population_buckets[10000000].append(city_info)
            elif population < 100000000:
                population_buckets[100000000].append(city_info)
            else:
                raise(Exception(f"Population {population} out of range"))


def main():
    print("Reading...")

    population_buckets[10] = []
    population_buckets[100] = []
    population_buckets[1000] = []
    population_buckets[10000] = []
    population_buckets[100000] = []
    population_buckets[1000000] = []
    population_buckets[10000000] = []
    population_buckets[100000000] = []

    read_csv_data()

    while True:
        """
        state_id = input("Enter a state: ").upper()

        print(cities_per_state[state_id])
        """

        """
        city = input("Enter a city: ")

        print(states_per_city[city])
        """

        pop = int(input("Enter population cap: "))

        print(population_buckets[pop])


if __name__ == "__main__":
    main()

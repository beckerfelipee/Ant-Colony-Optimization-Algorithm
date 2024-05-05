import random  # randomize actions
import time  # to skip function
import os  # To detect Operation System
import itertools  # create all possible sorts of an list
from geopy.distance import geodesic  # calculate distances with coordinates
from tqdm import tqdm  # To create visual loading bars
import c_data  # Us cities list

#                                   Config

# Running algorithms
ee_algorithm = True  # Exhaustive Enumeration
aco_algorithm = True  # Ant Colony Optimization

# Show options
show_cities = True
show_total_distance = True
show_ee_routes = False
show_ee_distances = False
show_aco_iterations = False

# ACO options
num_ants = 15
num_iterations = 30
alpha_value = 1
beta_value = 3
evaporation_rate = 0.1

#                                  Basic Functions

# Function that actualize the screen
def skip(sec):
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    time.sleep(sec)
    return os.system(command)


#  Function that calculates how close the ACO algorithm came to the optimal solution
def aco_accuracy(ee_result, aco_result):
    accuracy = (1 - (ee_result / aco_result)) * 100
    accuracy = '{:.2f}'.format(accuracy)
    return accuracy


#  Function that will calculate the distance between 2 cities
def dist(city1, city2):
    coords_1 = (city1.latitude, city1.longitude)
    coords_2 = (city2.latitude, city2.longitude)
    return geodesic(coords_1, coords_2).m


#                               Exhaustive Enumeration Functions

#  Calculate and find the best route using Exhaustive Enumeration
def exhaustive_enumeration(cities):
    distances = {}  # Create an empty dictionary to store distances
    print("EEA\nGenerating routes...")
    all_routes = list(itertools.permutations(cities))  # All possible routes
    if show_ee_routes:
        for r in all_routes:
            route_names = [city.name for city in r]
            print(route_names)
        print()
    best_route = (None, float('inf'))
    n_dist = 0
    print("Calculating distances..")

    if not show_ee_routes and not show_ee_distances:
        all_routes = tqdm(all_routes)  # generate a Loading bar

    for route in all_routes:
        distance = 0
        for i in range(len(route) - 1):  # cities distances
            city1, city2 = route[i], route[i + 1]
            if (city1, city2) in distances:  # For don´t have to calculate it again
                distance += distances[(city1, city2)]
            else:  # Calculate the distance
                dist_val = dist(city1, city2)
                distances[(city1, city2)] = dist_val  # put in the distances dictionary
                distances[(city2, city1)] = dist_val  # put in the distances dictionary
                distance += dist_val
                n_dist += 1  # Storage how many distances were calculated
                if show_ee_distances:
                    print("  ", distance)
        if route[0] != route[-1]:  # check if route ends in the starting point
            distance += dist(route[0], route[-1])  # add the distance from last point to starting point
            route = route + (route[0],)  # add the starting point to the end of the route
        if distance < best_route[1]:  # Calculate the best route
            best_route = (route, distance)
    print("done!\n")

    return best_route


#                             Ant Colony Optimization Functions

#  ACO variables
final_route_cost = 0
pheromones = []

#  Calculates the cost of a route (sum of distances between cities in route order)
def route_cost(route, cities):
    cost = 0
    for i in range(len(route) - 1):
        cost += dist(cities[route[i]], cities[route[i + 1]])
    cost += dist(cities[route[0]], cities[route[-1]])  # Add the cost of the return to the starting city
    return cost

#  Simulates an ant building a route
def build_route(cities, alpha=1, beta=1):

    # creates a list with city indices and shuffles
    remaining_cities = list(range(len(cities)))
    random.shuffle(remaining_cities)

    # initialize the route with the index of the first city
    route = [remaining_cities.pop(0)]
    while remaining_cities:  # while there are still cities to add to the route
        # calculates the probability of each city being chosen
        probs = []
        for i in remaining_cities:
            d = dist(cities[route[-1]], cities[i])
            probs.append((d ** (-beta)) * (pheromones[route[-1]][i] ** alpha))
        probs = [p / sum(probs) for p in probs]
        # choose the next city
        next_city = remaining_cities[random.choices(range(len(remaining_cities)), probs)[0]]
        route.append(next_city)
        remaining_cities.remove(next_city)
    route.append(route[0])  # Add the starting city at the end of the route
    return route

#  Function that runs the ant colony optimization algorithm
def ant_colony_optimization(cities, n_ants, n_iterations, alpha, beta, evaporation):
    global pheromones
    # initializes pheromones on all edges as a small amount
    pheromones = [[0.01 for _ in range(len(cities))] for _ in range(len(cities))]  # Generate a bi-dimensional matrix
    # the matrix is two-dimensional to be able to store and access the
    # pheromone values for each edge between each pair of cities.
    print("ACO\nGenerating ants...\nCreating ant´s iterations..")

    if not show_aco_iterations:
        range_iterations = tqdm(range(n_iterations))  # generate a Loading bar
    else:
        range_iterations = range(n_iterations)

    for i in range_iterations:  # for each iteration
        # store the routes built by ants
        routes = []
        # for each ant
        for j in range(n_ants):
            # build a route
            route = build_route(cities, alpha, beta)
            routes.append(route)
        # find the best iteration route
        best_route = min(routes, key=lambda x: route_cost(x, cities))
        if show_aco_iterations:
            print(best_route)
        # updates the pheromones on the edges of the best route
        for k in range(len(best_route) - 1):
            pheromones[best_route[k]][best_route[k + 1]] += 1 / route_cost(best_route, cities)
            pheromones[best_route[k + 1]][best_route[k]] += 1 / route_cost(best_route, cities)
        # evaporates a bit of pheromones on all edges
        for row in pheromones:
            for f in range(len(row)):
                row[f] *= 1 - evaporation
    print("done!\n")

    # Best route cost
    global final_route_cost
    final_route_cost = round(route_cost(best_route, cities)) / 1000

    # returns the best route found
    return [cities[i] for i in best_route]


#                                  Script

menu = True
while True:
    #  Menu
    while menu:
        aco_menu = False
        skip(0)
        print("\nAnt Colony Optimization Algorithm. "
              "\nArtificial Life. "
              "\nFelipe Becker "
              "\n\n"
              "                  Menu\n\n"
              "Running algorithms\n"
              f"[1] Exhaustive Enumeration Algorithm: {ee_algorithm}\n"
              f"[2] Ant Colony Optimization Algorithm: {aco_algorithm}\n"
              "\n"
              "Show options\n"
              f"[3] Show cities: {show_cities}\n"
              f"[4] Show total distance: {show_total_distance}\n"
              f"[5] Show EEA routes: {show_ee_routes}\n"
              f"[6] Show EEA distances: {show_ee_distances}\n"
              f"[7] Show ACO iterations: {show_aco_iterations}\n"
              "\n"
              f"[8] ACO MENU\n")

        select = input("Select an option or press [Enter] to continue: ")
        if select == "1":
            ee_algorithm = not ee_algorithm
        elif select == "2":
            aco_algorithm = not aco_algorithm
        elif select == "3":
            show_cities = not show_cities
        elif select == "4":
            show_total_distance = not show_total_distance
        elif select == "5":
            show_ee_routes = not show_ee_routes
        elif select == "6":
            show_ee_distances = not show_ee_distances
        elif select == "7":
            show_aco_iterations = not show_aco_iterations
        elif select == "8":
            aco_menu = True
        elif select == "":
            skip(1)
            break
        else:
            pass

        # ACO Menu
        while aco_menu:
            skip(0)
            print("\n\n"
                  "                ACO Menu\n\n"
                  f"[1] ants number = {num_ants}\n"
                  f"[2] iterations number = {num_iterations}\n"
                  f"[3] alpha value = {alpha_value}\n"
                  f"[4] beta value = {beta_value}\n"
                  f"[5] evaporation rate = {evaporation_rate}\n")
            select = input("Select an option or press [Enter] to go back: ")
            if select == "1":
                num_ants = int(input("\nEnter the number (10 - 100) of ants you want: "))
            elif select == "2":
                num_iterations = int(input("\nEnter the number (20 - 100) of iterations you want: "))
            elif select == "3":
                alpha_value = int(input("\nEnter the value (1 - 3) of alpha you want: "))
            elif select == "4":
                beta_value = int(input("\nEnter the value (1 - 3) of beta you want: "))
            elif select == "5":
                evaporation_rate = float(input("\nEnter the number (0.1 - 1.0) of evaporation you want: "))
            elif select == "":
                aco_menu = False
                break
            else:
                pass

    #  Choose the number of cities
    num_cities = int(input("How many cities will the salesman pass through?\n   "))
    selected_cities = c_data.cities[:num_cities]

    #  Show the selected cities
    if show_cities:
        print("\nCities: ")
        for city in selected_cities:
            print("  ", city)
        print()

    #                            Run the Algorithms

    #  use Exhaustive Enumeration Algorithm
    if ee_algorithm:
        ee_start_time = time.perf_counter()
        # Run the Algorithm
        ee_best_route = exhaustive_enumeration(selected_cities)
        ee_end_time = time.perf_counter()
        ee_elapsed_time = ee_end_time - ee_start_time

    time.sleep(1)

    #  use Ant Colony Optimization Algorithm
    if aco_algorithm:
        aco_start_time = time.perf_counter()
        # Run the Algorithm
        aco_best_route = ant_colony_optimization(selected_cities, num_ants, num_iterations,
                                                 alpha_value, beta_value, evaporation_rate)
        aco_end_time = time.perf_counter()
        aco_elapsed_time = aco_end_time - aco_start_time

    # Show Results

    print("------------------------------------------------------------\n")

    if ee_algorithm:
        print("Exhaustive Enumeration Algorithm results: \n")
        print("Processing time:", ee_elapsed_time)
        print("Best route:", [city.name for city in ee_best_route[0]])  # Show the best route
        if show_total_distance:  # Show the total distance of the best route
            print("Total distance:", round(ee_best_route[1]) / 1000, "km\n")

    if aco_algorithm:
        print("Ant Colony Optimization Algorithm results: \n")
        print("Processing time:", aco_elapsed_time)
        print("Best route:", [city.name for city in aco_best_route])  # Show the best route
        if show_total_distance:  # Show the total distance of the best route
            print("Total distance:", final_route_cost, "km")
        if ee_algorithm:
            aco_deviation = aco_accuracy(round(ee_best_route[1]) / 1000, final_route_cost)
            print(f"Optimal solution deviation: {aco_deviation}%")

    restart = input("\nPress [Enter] to continue or type [x] to finish the program..\n")
    if restart == "x":
        break

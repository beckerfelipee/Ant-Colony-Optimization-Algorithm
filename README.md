# Ant-Colony-Optimization-Algorithm
This project aims to create and implement the Ant Colony Optimization (ACO) algorithm to solve the Traveling Salesman Problem (TSP), an NP-hard problem. The TSP involves finding the shortest route that visits all cities in a set and returns to the starting city. As the complexity of the problem grows exponentially with the number of cities, exhaustive search methods become impractical for large-scale problems.

## Objectives
- Implement the ACO algorithm to solve the TSP.
- Compare the performance of the ACO algorithm with an exhaustive enumeration (EE) algorithm in terms of result accuracy and processing time.
- Utilize the TSP as a test problem, considering a sample of cities from the United States with real coordinates obtained through Google Maps geolocation.
- Evaluate the algorithms' performance in terms of total distance traveled and execution time.
  
## Methodology
### Exhaustive Enumeration (EE) Algorithm
- Data Collection: Collect data from cities, including name, latitude, and longitude.
- Generation of Possible Routes: Generate all possible combinations of routes.
- Calculation of Distances: Calculate the total distance for each generated route.
- Identification of the Best Route: Select the route with the shortest total distance.
### Ant Colony Optimization (ACO) Algorithm
- Data Collection: Use the same list of cities used by the EE algorithm.
- [Creation of Route Construction Function](google.com): Simulate the construction of a route by an ant, using probability calculations based on distance and pheromone level.
- Initialization of Pheromone: Initialize the pheromones on all edges with a small amount.
- Iteration Execution: Execute a defined number of iterations, where each ant constructs a route.
- Identification of the Best Route of the Iteration and Pheromone Update: Choose the best route of the iteration and update the pheromones on the edges.
- Identification of the Global Best Route: Return the best route found after all iterations.

## Results
According to the study results, the ACO algorithm showed a shorter processing time than the EE algorithm from 8 cities onwards. However, the EE algorithm was more efficient for a smaller number of cities. The best routes generated by the ACO were close to the best routes generated by the EE, especially with a small number of cities. The deviations of the best routes from the ACO compared to the optimal solution remained below 3% during all tests.

## Conclusion
The ACO algorithm demonstrated effectiveness in solving the TSP, being able to handle up to 18 cities with relative ease. It is expected that the ACO can handle routes with an even larger number of cities, although adjusting the number of iterations and ants may be necessary to maintain the algorithm's accuracy. The study reinforces the advantage of heuristic algorithms like ACO over exhaustive search in NP-hard problems, especially in terms of processing time.


### To develop the ant colony optimization algorithm, the following steps were performed:

#### 1. Data Collection:
Data for cities are collected from the same list used by the first algorithm.

#### 2. Creation of a Function Simulating Ant Route Construction:
The route of an ant starts from a random city, and then the probability of each city being chosen as the next one is calculated. 
The probability is computed by taking the distance between the current city in the route and the next city to the power of **-β**, where **β** is the parameter influencing the distance for the ant. 
This value is multiplied by the pheromone level on the edge between the current city and the next city to the power of **α**, where α is the parameter influencing the pheromone for the ant. 
Thus, this function can be formulated as follows:

![formula](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/3a51553d-4d98-4349-9055-fe6c2f559f1a)

Where:
- ![image](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/11c4b902-fd91-4874-ba56-b28810ac6b5e) is the probability of ant **k** going from city **x** to city **y**.
- ![image](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/5241cfa3-c30d-4896-8f6f-70d58f7607bb) is the distance between city **x** and city **y**.
- ![image](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/82b5dba3-b894-4915-bcbf-2c0e88d26944) is the parameter influencing the distance for the ant.
- ![image](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/ab7238a4-2125-4297-9a86-34593cf36681) is the amount of pheromone deposited on the edge between cities **x** and **y**.
- ![image](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/9d3bdc22-e772-4a33-8970-bb93edf5444a) is the parameter influencing the pheromone for the ant.

The negative exponent in ![image](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/17adb5a2-8961-4e6e-8774-467ecabef443) is used to invert the distance. 
Thus, if ![image](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/5241cfa3-c30d-4896-8f6f-70d58f7607bb) has a high value, the probability will be small, and if it has a low value, the probability will be large.

The variables **β** and **α** are parameters that can be adjusted to control the relative importance of distance and pheromone level in the probability calculation. 
A higher value of **β** gives more weight to the distance, while a higher value of **α** gives more weight to the pheromone level.

The calculation of ![image](https://github.com/beckerfelipee/Ant-Colony-Optimization-Algorithm/assets/94445094/5241cfa3-c30d-4896-8f6f-70d58f7607bb) uses the geopy library to handle coordinate information and perform the calculation. 

After all cities are chosen, the route is returned.

#### 3. Initialization of Pheromones:
The algorithm starts by initializing the pheromones on all edges with a small amount. 
Pheromones are used to store information about the quality of routes that ants have previously made. 
In this case, pheromones are represented by a two-dimensional matrix, where each element represents the pheromone level on the edge between a pair of cities.

#### 4. Iteration Execution:
The algorithm executes a defined number of iterations, where in each iteration, a certain number of ants are generated. 
Each ant constructs a route using the function mentioned earlier, which employs a probability calculation based on distance and pheromone level to determine the next city to be added to the route. 
The routes built by the ants are stored in a list.

#### 5. Identification of the Best Route of the Iteration and Pheromone Update:
After all ants have constructed their routes in an iteration, the best route among the set (the one with the lowest cost) is chosen, and the pheromones on the edges of the best route are updated. 
Specifically, the pheromones are incremented by a value proportional to the inverse of the route cost, meaning that the edges of the best route will receive more pheromones, and the edges of a poor route will receive fewer. 
After this, the pheromones on all edges are evaporated by a small amount (specified by the evaporation parameter) to simulate the natural decay of pheromones. 
This encourages ants to explore new routes in subsequent iterations.

#### 6. Identification and Return of the Best Route:
After all iterations are completed, the algorithm returns the best route found among the set of best routes and also calculates the cost of this route.

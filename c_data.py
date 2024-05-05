class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"City: {self.name}, Latitude: {self.latitude}, Longitude: {self.longitude}"


cities = [City("New York", 40.730610, -73.935242),
          City("Los Angeles", 34.052235, -118.243683),
          City("Chicago", 41.875562, -87.624421),
          City("Houston", 29.758938, -95.367697),
          City("Phoenix", 33.448376, -112.074036),
          City("Philadelphia", 39.952583, -75.165222),
          City("San Antonio", 29.424122, -98.493628),
          City("San Diego", 32.715329, -117.157255),
          City("Dallas", 32.776664, -96.796988),
          City("San Jose", 37.338208, -121.886329),
          City("Austin", 30.267153, -97.743061),
          City("Jacksonville", 30.332184, -81.655651),
          City("Fort Worth", 32.725409, -97.320849),
          City("Columbus", 39.961176, -82.998794),
          City("San Francisco", 37.774929, -122.419416),
          City("Charlotte", 35.227087, -80.843127),
          City("Indianapolis", 39.768403, -86.158068),
          City("Seattle", 47.608013, -122.335167)]

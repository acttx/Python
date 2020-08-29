from graph import Graph
from road import Road
from city import City

"""
For this program:
  1. Create the City and Road lists 
  2. Add 6 City objects to the City (Vertex) list.
  3. Add 18 Road objects to the Road (Edge) list.  
  4. Create a Graph passing in the City and Road lists.
  5. Using the Graph you created: 
     Display each of the items requested below:
     (Use Graph methods to do these, wherever possible)
     a. The number of Cities in the map; use Graph method.
     b. The City object information for the 4th City
        added, using a Graph method to retrieve the City.
     c. The City (Vertex) with the largest number of neighbors
     d. Print the City and Road information using a Graph method
        to retrieve the City and Roads. 
"""


def main():
    """
    The NCCitiesRoads mainline logic creates a graph 
    from city and road information
    """
    
    # Create a list of City and Road objects

    cities = []
    roads = []

    # Create 6 Cities

    murphy = City("Murphy", -84.029924, 35.089848, 1627)
    mars_hill = City("Mars Hill", -82.547843, 35.828496, 1869)
    mooresville = City("Mooresville", -80.820139, 35.584337, 32711)
    morrisville = City("Morrisville", -78.828930, 35.827493, 18576)
    morehead_city = City("Morehead City", -76.746748, 34.727700, 8661)
    manteo = City("Manteo", -75.669385, 35.904595, 1434)

    # Add them to list

    cities.append(murphy)
    cities.append(mars_hill)
    cities.append(mooresville)
    cities.append(morrisville)
    cities.append(morehead_city)
    cities.append(manteo)

    # Create 18 roads and add them to list

    r0 = Road(murphy, mars_hill)
    r1 = Road(murphy, mooresville)

    r2 = Road(mars_hill, murphy)
    r3 = Road(mars_hill, mooresville)
    r4 = Road(mars_hill, morrisville)

    r5 = Road(mooresville, murphy)
    r6 = Road(mooresville, mars_hill)
    r7 = Road(mooresville, morrisville)
    r8 = Road(mooresville, morehead_city)

    r9 = Road(morrisville, mars_hill)
    r10 = Road(morrisville, mooresville)
    r11 = Road(morrisville, morehead_city)
    r12 = Road(morrisville, manteo)

    r13 = Road(morehead_city, mooresville)
    r14 = Road(morehead_city, morrisville)
    r15 = Road(morehead_city, manteo)

    r16 = Road(manteo, morrisville)
    r17 = Road(manteo, morehead_city)

    # add roads to list
    for i in range(0, 18):
        roads.append(eval("r" + str(i)))

    # a. Print the number of cities in the map, using a Graph method

    map_graph = Graph(cities, roads)
    print("The number of cities: ", str(map_graph.get_size()))
    print()

    # b. Print the City object information for the 4th city,
    # using Graph methods to retrieve the City, with index 3.

    print(map_graph.vertices[3])
    print()

    # c. Determine the City with the largest number 
    # of Roads ending there and print the City name
    # Use the Graph method that helps with this.

    largest_num_roads_city = ""
    amt_roads = 0
    roads_count = 0

    for city in cities:
        for road in map_graph.neighbors_dict.get(city.get_name()):
            roads_count += 1
        if roads_count > amt_roads:
            largest_num_roads_city = city.get_name()
            amt_roads = roads_count
        roads_count = 0
    print("City with the most roads: ", largest_num_roads_city)
    print()

    # d. Print the City and Road edge information using a Graph method.
    # to retrieve the City and Roads
    print("Road information:")
    print()
    for city in cities:
        print("City:", city)
        for road in map_graph.neighbors_dict.get(city.get_name()):
            print(road)
        print()


main()

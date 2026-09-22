fr = open("bus_vytazenost.txt", "r")

capacity = int(fr.readline().strip())
 
counter = 0
stops = []
overloaded_stops = []
max_overflow = 0
occupancy = 0
 
for row in fr:
    processed_row = row.strip().split(" ")
    nastupujuci = int(processed_row[0])
    vystupujuci = int(processed_row[1])
    stop_name = " ".join(processed_row[2:])
    stops.append(stop_name)
    occupancy = occupancy - vystupujuci + nastupujuci
    if occupancy > capacity:
        overloaded_stops.append(stop_name)
        overflow = occupancy - capacity
        if overflow > max_overflow:
            max_overflow = overflow
 
    print(processed_row)
    counter += 1
 
print(f"Počet zastávok na trase je: {counter}\n")
print(f"Zastávky sú: {', '.join(stops)}\n")
 
if overloaded_stops:
    print(f"Preplnené zastávky sú: {', '.join(overloaded_stops)}\n")
    print(f"Najvyšší počet ľudí nad rámec kapacity je: {max_overflow}\n")
else:
    print("Kapacita autobusu nebola na trase nikde prekročená.\n")
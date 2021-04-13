# Given an unordered list of flights taken by someone, each represented as [origin, destination] pairs. Write a Python
# program to return persons destination.

def destination_city(flights):
    strt = []
    dstn = []
    for fl in flights:
        strt.append(fl[0])
        dstn.append(fl[1])

    for city in dstn:
        if city not in strt:
            return city

paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print(destination_city(paths))
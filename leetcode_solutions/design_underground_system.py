"""
1396. Design Underground System

Medium

https://leetcode.com/problems/design-underground-system/description/
"""


class UndergroundSystem:
    def __init__(self):
        self.customers = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.customers[id]
        self.customers.pop(id)
        route_id = f"{start_station}-{stationName}"
        if route_id not in self.routes.keys():
            total_time = 0
            count = 0
        else:
            total_time, count = self.routes[route_id]
        self.routes[route_id] = (total_time + t - check_in_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route_id = f"{startStation}-{endStation}"
        return self.routes[route_id][0] / self.routes[route_id][1]


class UndergroundSystemV2:
    """
    Explicit but less efficient alternative
    """

    def __init__(self):
        self.customers = {}
        self.routes = {}

    def checkIn(self, id: int, station_name: str, t: int) -> None:
        self.customers[id] = {'start_time': t, 'start_station': station_name}

    def checkOut(self, id: int, station_name: str, t: int) -> None:
        self.customers[id] = {**self.customers[id], **{'end_time': t, 'end_station': station_name}}
        route_id = f"{self.customers[id]['start_station']}-{self.customers[id]['end_station']}"
        if route_id not in self.routes.keys():
            total_time = 0
            count = 0
        else:
            total_time = self.routes[route_id]['total_time']
            count = self.routes[route_id]['count']
        self.routes[route_id] = {'total_time': total_time + t - self.customers[id]['start_time'],
                                 'count': count + 1}

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        route_id = f"{start_station}-{end_station}"
        return self.routes[route_id]['total_time'] / self.routes[route_id]['count']


if __name__ == '__main__':
    # Case 1
    obj = UndergroundSystem()
    obj.checkIn(45, 'Leyton', 3)
    obj.checkIn(32, 'Paradise', 8)
    obj.checkIn(27, 'Leyton', 10)
    obj.checkOut(45, 'Waterloo', 15)
    obj.checkOut(27, 'Waterloo', 20)
    obj.checkOut(32, 'Cambridge', 22)
    avg_time_1 = obj.getAverageTime('Paradise', 'Cambridge')
    avg_time_2 = obj.getAverageTime('Leyton', 'Waterloo')
    obj.checkIn(10, 'Leyton', 24)
    avg_time_3 = obj.getAverageTime('Leyton', 'Waterloo')
    obj.checkOut(10, 'Waterloo', 38)
    avg_time_4 = obj.getAverageTime('Leyton', 'Waterloo')

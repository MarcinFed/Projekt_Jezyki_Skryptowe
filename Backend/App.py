from Backend.Travel import Travel


class App:
    def __init__(self):
        self.__travels = []

    def add_travel(self, name, destination, start_date, end_date):
        travel = Travel(name, destination, start_date, end_date)
        self.__travels.append(travel)

    @property
    def travels(self):
        return self.__travels


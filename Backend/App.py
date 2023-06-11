from Backend.Travel import Travel
import pickle
import os


class App:
    def __init__(self):
        self.__travels = []
        self.__filename = "Saves\\travels.plan"

    def add_travel(self, name, destination, start_date, end_date):
        travel = Travel(name, destination, start_date, end_date)
        self.__travels.append(travel)

    @property
    def travels(self):
        return self.__travels

    def save_to_file(self):
        data = {
            'travels': self.__travels,
        }
        with open(self.__filename, "wb") as file:
            pickle.dump(data, file)

    def load_from_file(self):
        with open(self.__filename, "rb") as file:
            data = pickle.load(file)
        self.__travels = data['travels']



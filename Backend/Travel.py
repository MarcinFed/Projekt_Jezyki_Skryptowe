from Backend.Plan import Plan
from Backend.Transport import Transport
from Backend.Accommodation import Accommodation
from Backend.Localization import Localization
from datetime import datetime


class Travel:
    def __init__(self, name, destination, start_date, end_date):
        self.__name = name
        self.__destination = destination
        self.__start_date = start_date
        self.__end_date = end_date
        self.__days = (end_date - start_date).days
        self.__transport_to = None
        self.__transport_from = None
        self.__accommodation = None
        self.__plan = None

    @property
    def plan(self):
        return self.__plan

    @plan.setter
    def plan(self):
        self.__plan = Plan()

    @property
    def transport_to(self):
        return self.__transport_to

    @transport_to.setter
    def transport_to(self, values):
        transport_type, departure_time, time, ticket = values
        self.__transport_to = Transport(transport_type, departure_time, time, ticket)

    @property
    def transport_from(self):
        return self.__transport_from

    @transport_from.setter
    def transport_from(self, values):
        transport_type, departure_time, time, ticket = values
        self.__transport_from = Transport(transport_type, departure_time, time, ticket)

    @property
    def accommodation(self):
        return self.__accommodation

    @accommodation.setter
    def accommodation(self, values):
        name, city, post_code, street, building, apartment = values
        self.__accommodation = Accommodation(name, Localization(city, post_code, street, building, apartment))

    @property
    def name(self):
        return self.__name

    @property
    def destination(self):
        return self.__destination

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @property
    def days(self):
        return self.__days

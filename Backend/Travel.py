from Backend.Plan import Plan
from Backend.Transport import Transport
from Backend.Accommodation import Accommodation
from Backend.Localization import Localization
from datetime import datetime


class Travel:
    def __init__(self, name, destination, start_date, end_date):
        self.name = name
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.days = (end_date - start_date).days
        self.transport_to = None
        self.transport_from = None
        self.accommodation = None
        self.plan = None

    def make_plan(self):
        self.plan = Plan()

    def set_transport_to(self, transport_type, departure_time, time, ticket=None):
        self.transport_to = Transport(transport_type, departure_time, time, ticket)

    def set_transport_from(self, transport_type, departure_time, time, ticket=None):
        self.transport_from = Transport(transport_type, departure_time, time, ticket)

    def set_accommodation(self, name, city, post_code, street, building, apartment):
        self.accommodation = Accommodation(name, Localization(city, post_code, street, building, apartment))

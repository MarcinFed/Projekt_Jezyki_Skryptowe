from Backend.Localization import Localization


class Activity:
    def __init__(self, name, start_hour, end_hour, ticket_needed=False, pdf_ticket=None, localization=None):
        self.__name = name
        self.__start_hour = start_hour
        self.__end_hour = end_hour
        self.__ticket_needed = ticket_needed
        self.__pdf_ticket = pdf_ticket
        self.__localization = localization

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def start_hour(self):
        return self.__start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        self.__start_hour = start_hour

    @property
    def end_hour(self):
        return self.__end_hour

    @end_hour.setter
    def end_hour(self, end_hour):
        self.__end_hour = end_hour

    @property
    def ticket_needed(self):
        return self.__ticket_needed

    @ticket_needed.setter
    def ticket_needed(self, ticket_needed):
        self.__ticket_needed = ticket_needed

    @property
    def pdf_ticket(self):
        return self.__pdf_ticket

    @pdf_ticket.setter
    def pdf_ticket(self, pdf_ticket):
        self.__pdf_ticket = pdf_ticket

    @property
    def localization(self):
        return self.__localization

    @localization.setter
    def localization(self, localization):
        city, street, post, building, apartment = localization
        self.__localization = Localization(city, street, post, building, apartment)

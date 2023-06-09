class Transport:
    def __init__(self, transport_type, departure_hour, time, pdf_ticket=None):
        self.__transport_type = transport_type
        self.__departure_hour = departure_hour
        self.__time = time
        self.__pdf_ticket = pdf_ticket

    @property
    def transport_type(self):
        return self.__transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        self.__transport_type = transport_type

    @property
    def departure_hour(self):
        return self.__departure_hour

    @departure_hour.setter
    def departure_hour(self, departure_hour):
        self.__departure_hour = departure_hour

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    @property
    def pdf_ticket(self):
        return self.__pdf_ticket

    @pdf_ticket.setter
    def pdf_ticket(self, pdf_ticket):
        self.__pdf_ticket = pdf_ticket

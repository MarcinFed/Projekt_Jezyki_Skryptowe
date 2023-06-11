import vobject
import datetime


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

    def add_to_calendar(self, calendar, date):
        transport = calendar.add("vevent")
        transport.add("summary").value = self.__transport_type

        start_datetime, end_datetime = self.prepare_time(date)

        transport.add("dtstart").value = start_datetime
        transport.add("dtend").value = end_datetime

    def prepare_time(self, date):
        start_time = datetime.datetime.strptime(self.__departure_hour, "%H:%M").time()
        start_datetime = datetime.datetime.combine(date, start_time)

        end_time = datetime.datetime.strptime(self.__departure_hour, "%H:%M").time()
        end_offset = datetime.timedelta(hours=float(self.__time.replace(",", ".")))
        end_datetime = datetime.datetime.combine(date, end_time) + end_offset

        return start_datetime, end_datetime
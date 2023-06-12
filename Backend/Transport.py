import datetime


class Transport:  # Class that stores the transport data
    def __init__(self, transport_type, departure_hour, time, pdf_ticket=None):
        self.__transport_type = transport_type  # Initializing the transport type
        self.__departure_hour = departure_hour  # Initializing the departure hour
        self.__time = time  # Initializing the travel time
        self.__pdf_ticket = pdf_ticket  # Initializing the PDF ticket (optional)

    @property
    def transport_type(self):  # Getter method to access the transport type
        return self.__transport_type

    @transport_type.setter
    def transport_type(self, transport_type):  # Setter method to update the transport type
        self.__transport_type = transport_type

    @property
    def departure_hour(self):  # Getter method to access the departure hour
        return self.__departure_hour

    @departure_hour.setter
    def departure_hour(self, departure_hour):  # Setter method to update the departure hour
        self.__departure_hour = departure_hour

    @property
    def time(self):  # Getter method to access the travel time
        return self.__time

    @time.setter
    def time(self, time):  # Setter method to update the travel time
        self.__time = time

    @property
    def pdf_ticket(self):  # Getter method to access the PDF ticket
        return self.__pdf_ticket

    @pdf_ticket.setter
    def pdf_ticket(self, pdf_ticket):  # Setter method to update the PDF ticket
        self.__pdf_ticket = pdf_ticket

    def add_to_calendar(self, calendar, date):  # Method to add transport to the calendar plan
        transport = calendar.add("vevent")  # Adding a new event for the transport to the calendar
        transport.add("summary").value = self.__transport_type  # Setting the summary of the event to the transport type

        start_datetime, end_datetime = self.prepare_time(date)  # Preparing the start and end datetimes for the event

        transport.add("dtstart").value = start_datetime  # Setting the start datetime of the event
        transport.add("dtend").value = end_datetime  # Setting the end datetime of the event

    def prepare_time(self, date):  # Method for preparing the date and time to specified format
        start_time = datetime.datetime.strptime(self.__departure_hour, "%H:%M").time()  # Parsing the departure hour as a time object
        start_datetime = datetime.datetime.combine(date, start_time)  # Combining the date and departure time for the event

        end_time = datetime.datetime.strptime(self.__departure_hour, "%H:%M").time()  # Parsing the departure hour as a time object
        end_offset = datetime.timedelta(hours=float(self.__time.replace(",", ".")))  # Calculating the time offset for the end datetime
        end_datetime = datetime.datetime.combine(date, end_time) + end_offset  # Combining the date, departure time, and time offset for the event

        return start_datetime, end_datetime  # Returning the start and end datetimes for the event
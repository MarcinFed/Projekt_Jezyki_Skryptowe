from Backend.Plan import Plan  # Importing the Plan class from the Backend.Plan module
from Backend.Transport import Transport  # Importing the Transport class from the Backend.Transport module
from Backend.Accommodation import Accommodation  # Importing the Accommodation class from the Backend.Accommodation module
from Backend.Localization import Localization  # Importing the Localization class from the Backend.Localization module
import os  # Importing the os module for file operations
import vobject  # Importing the vobject module for working with iCalendar data
import datetime  # Importing the datetime module for working with dates and times


class Travel:  # Class that stores one specified travel data
    def __init__(self, name, destination, start_date, end_date):
        self.__name = name  # Initializing the name of the travel
        self.__destination = destination  # Initializing the destination of the travel
        self.__start_date = start_date  # Initializing the start date of the travel
        self.__end_date = end_date  # Initializing the end date of the travel
        self.__days = (end_date - start_date).days  # Calculating the number of days for the travel
        self.__transport_to = None  # Initializing the transport to the destination as None
        self.__transport_from = None  # Initializing the transport from the destination as None
        self.__accommodation = None  # Initializing the accommodation for the travel as None
        self.__plan = Plan(self.__start_date, self.__end_date, self.__destination)  # Creating a Plan object for the travel
        self.__medium_temp = self.get_medium_temperature()  # Setting the medium temperature for the travel

    @property
    def plan(self):  # Getter method to access the plan of the travel
        return self.__plan

    @property
    def transport_to(self):  # Getter method to access the transport to the destination
        return self.__transport_to

    @transport_to.setter
    def transport_to(self, values):  # Setter method to set the transport to the destination
        transport_type, departure_time, time, ticket = values
        self.__transport_to = Transport(transport_type, departure_time, time, ticket)

    @property
    def transport_from(self):  # Getter method to access the transport from the destination
        return self.__transport_from

    @transport_from.setter
    def transport_from(self, values):  # Setter method to set the transport from the destination
        transport_type, departure_time, time, ticket = values
        self.__transport_from = Transport(transport_type, departure_time, time, ticket)

    @property
    def accommodation(self):  # Getter method to access the accommodation for the travel
        return self.__accommodation

    @accommodation.setter
    def accommodation(self, values):  # Setter method to set the accommodation for the travel
        name, city, post_code, street, building, apartment = values
        self.__accommodation = Accommodation(name, Localization(city, post_code, street, building, apartment))

    @property
    def name(self):  # Getter method to access the name of the travel
        return self.__name

    @property
    def destination(self):  # Getter method to access the destination of the travel
        return self.__destination

    @property
    def start_date(self):  # Getter method to access the start date of the travel
        return self.__start_date

    @property
    def end_date(self):  # Getter method to access the end date of the travel
        return self.__end_date

    @property
    def days(self):  # Getter method to access the number of days of the travel
        return self.__days

    @property
    def medium_temp(self):  # Getter method to access the medium temperature for the travel
        return self.__medium_temp

    def get_medium_temperature(self):  # Method to get medium temperature for the trip
        temps = []
        for day in self.__plan.days:
            temps.append(day.temperature)  # Collecting temperatures for each day in the plan

        average = sum(temps)/len(temps)  # Calculating the average temperature
        formatted_average = f"{average:.1f}"  # Formatting the average temperature with one decimal place
        return formatted_average  # Returning the formatted average temperature

    def add_to_calendar(self):  # Method to generate calendar plan
        calendar = vobject.iCalendar()  # Creating a new iCalendar object

        travel = calendar.add("vevent")  # Adding a new event to the calendar
        travel.add("summary").value = self.name  # Setting the summary of the event to the travel name
        travel.add("location").value = self.destination  # Setting the location of the event to the travel destination
        travel.add("description").value = self.accommodation.name  # Setting the description of the event to the accommodation name

        start_datetime, end_datetime = self.prepare_time()  # Preparing the start and end datetimes for the event

        travel.add("dtstart").value = start_datetime  # Setting the start datetime of the event
        travel.add("dtend").value = end_datetime  # Setting the end datetime of the event

        self.transport_to.add_to_calendar(calendar, self.start_date)  # Adding the transport to the calendar
        self.transport_from.add_to_calendar(calendar, self.end_date)  # Adding the transport from the calendar

        self.__plan.add_to_calendar(calendar)  # Adding the plan to the calendar

        calendar_path = "Calendar\\"+self.name+".ics"  # Generating the file path for saving the calendar file

        if not os.path.exists("Calendar"):  # Checking if the 'Calendar' directory exists, if not, creating it
            os.makedirs("Calendar")

        with open(calendar_path, "w", encoding='utf-8') as file:  # Opening the file for writing the calendar data
            file.write(calendar.serialize())  # Serializing and writing the calendar data to the file

    def prepare_time(self):  # Method for preparing the date and time data to specified format
        to_departure_time = datetime.datetime.strptime(self.transport_to.departure_hour, "%H:%M").time()  # Parsing the departure time for transport to the destination
        start_datetime = datetime.datetime.combine(self.start_date, to_departure_time)  # Combining the start date and departure time for the event

        from_departure_time = datetime.datetime.strptime(self.transport_from.departure_hour, "%H:%M").time()  # Parsing the departure time for transport from the destination
        time_offset = datetime.timedelta(hours=float(0 if self.transport_from.time == "" else self.transport_from.time))  # Calculating the time offset for the end datetime
        end_datetime = datetime.datetime.combine(self.end_date, from_departure_time) + time_offset  # Combining the end date, departure time, and time offset for the event

        return start_datetime, end_datetime  # Returning the start and end datetimes for the event

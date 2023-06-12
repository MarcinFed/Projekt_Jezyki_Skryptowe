from Backend.Localization import Localization
import datetime


class Activity:  # Class that stores the activity data
    def __init__(self, name, start_hour, end_hour, ticket_needed=False, pdf_ticket=None, localization=None):
        self.__name = name  # Initializing the name of the activity
        self.__start_hour = start_hour  # Initializing the start hour of the activity
        self.__end_hour = end_hour  # Initializing the end hour of the activity
        self.__ticket_needed = ticket_needed  # Initializing whether a ticket is needed for the activity
        self.__pdf_ticket = pdf_ticket  # Initializing the PDF ticket for the activity
        self.__localization = localization  # Initializing the localization of the activity

    @property
    def name(self):  # Getter method to access the name of the activity
        return self.__name

    @name.setter
    def name(self, name):  # Setter method to update the name of the activity
        self.__name = name

    @property
    def start_hour(self):  # Getter method to access the start hour of the activity
        return self.__start_hour

    @start_hour.setter
    def start_hour(self, start_hour):  # Setter method to update the start hour of the activity
        self.__start_hour = start_hour

    @property
    def end_hour(self):  # Getter method to access the end hour of the activity
        return self.__end_hour

    @end_hour.setter
    def end_hour(self, end_hour):  # Setter method to update the end hour of the activity
        self.__end_hour = end_hour

    @property
    def ticket_needed(self):  # Getter method to check if a ticket is needed for the activity
        return self.__ticket_needed

    @ticket_needed.setter
    def ticket_needed(self, ticket_needed):  # Setter method to update whether a ticket is needed
        self.__ticket_needed = ticket_needed

    @property
    def pdf_ticket(self):  # Getter method to access the PDF ticket for the activity
        return self.__pdf_ticket

    @pdf_ticket.setter
    def pdf_ticket(self, pdf_ticket):  # Setter method to update the PDF ticket for the activity
        self.__pdf_ticket = pdf_ticket

    @property
    def localization(self):  # Getter method to access the localization of the activity
        return self.__localization

    @localization.setter
    def localization(self, localization):  # Setter method to update the localization
        city, street, post, building, apartment = localization
        self.__localization = Localization(city, street, post, building, apartment)

    def add_to_calendar(self, calendar, date):  # Method to add activity to calendar plan
        activity = calendar.add("vevent")  # Create a new vevent in the calendar
        activity.add("summary").value = self.name  # Set the summary of the activity

        start_datetime, end_datetime = self.prepare_time(date)  # Prepare the start and end datetime

        activity.add("dtstart").value = start_datetime  # Set the start datetime of the activity
        activity.add("dtend").value = end_datetime  # Set the end datetime of the activity

    def prepare_time(self, date):
        start_time = datetime.datetime.strptime(self.start_hour, "%H:%M").time()  # Convert start hour to time object
        start_datetime = datetime.datetime.combine(date, start_time)  # Combine date and start time

        end_time = datetime.datetime.strptime(self.end_hour, "%H:%M").time()  # Convert end hour to time object
        end_datetime = datetime.datetime.combine(date, end_time)  # Combine date and end time

        return start_datetime, end_datetime

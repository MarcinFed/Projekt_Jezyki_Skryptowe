from Backend.Day import Day
from datetime import timedelta
from mtranslate import translate


class Plan:  # Class that stores the plan data
    def __init__(self, start_date, end_date, city):
        self.__start_date = start_date  # Initializing the start date of the plan
        self.__end_date = end_date  # Initializing the end date of the plan
        self.__days = []  # Initializing an empty list to store the days of the plan
        self.__city = city  # Initializing the city associated with the plan
        self.make_days()  # Creating the days of the plan

    @property
    def start_date(self):  # Getter method to access the start date of the plan
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):  # Setter method to update the start date of the plan
        self.__start_date = start_date

    @property
    def end_date(self):  # Getter method to access the end date of the plan
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):  # Setter method to update the end date of the plan
        self.__end_date = end_date

    @property
    def days(self):  # Getter method to access the list of days in the plan
        return self.__days

    @days.setter
    def days(self, day):  # Setter method to add an activity to a specific day
        self.__days[day].add_activity()

    def make_days(self):  # Method that makes single days inside the plan
        current_date = self.__start_date
        while current_date <= self.__end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")  # Format the date
            day_of_week = self.translate_day_of_week(current_date.strftime("%A"))  # Setting the day_of_week name
            new_day = Day(formatted_date, day_of_week, self.__city)  # Creating a new day
            self.__days.append(new_day)  # Adding a new day to the plan
            current_date += timedelta(days=1)  # Moving to the next day

    def translate_day_of_week(self, day_of_week):  # Method for translating the day of week from English to Polish
        translation = translate(day_of_week, "pl", "en")  # Translating the day of the week to Polish
        return translation

    def add_to_calendar(self, calendar):  # Method for adding the plan to calendar plan
        for day in self.__days:
            day.add_to_calendar(calendar)  # Adding each day to the calendar

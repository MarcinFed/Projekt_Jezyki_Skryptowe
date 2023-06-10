from Backend.Activity import Activity
from Backend.Day import Day
from datetime import datetime, timedelta
from mtranslate import translate


class Plan:
    def __init__(self, start_date, end_date, city):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__days = []
        self.__city = city
        self.make_days()

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        self.__start_date = start_date

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        self.__end_date = end_date

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, day, activity):
        self.__days[day].add_activity()

    def make_days(self):
        current_date = self.__start_date
        while current_date <= self.__end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")
            day_of_week = self.translate_day_of_week(current_date.strftime("%A"))
            new_day = Day(formatted_date, day_of_week, self.__city)
            self.__days.append(new_day)
            current_date += timedelta(days=1)

    def translate_day_of_week(self, day_of_week):
        translation = translate(day_of_week, "pl", "en")
        return translation

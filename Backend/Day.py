import requests
from datetime import datetime
from mtranslate import translate
from Backend.Activity import Activity
from Backend.Localization import Localization


class Day:  # Class that stores the day data
    def __init__(self, date, day, city):
        self.__date = datetime.strptime(date, "%Y-%m-%d")  # Initializing the date of the day
        self.__day = day  # Initializing the day of the week
        self.__city = city  # Initializing the city associated with the day
        self.__activities = []  # Initializing an empty list to store activities
        self.__temperature = self.forecast_weather(self.__city, date)  # Fetching the forecasted temperature

    @property
    def temperature(self):  # Getter method to access the temperature of the day
        return self.__temperature

    def forecast_weather(self, pl_city, date):  # Method for getting the forecast weather for the dat
            api_key = ""  # API key for weather forecast
            city = self.translate_city(pl_city)  # Translating the city name to English

            target_date = datetime.strptime(date, "%Y-%m-%d")
            today = datetime.today()

            if (target_date.date() - today.date()).days > 10:  # If the day is not within the next 10 days then get historical weather
                previous_year = target_date.year - 1
                modified_date = target_date.replace(year=previous_year).strftime("%Y-%m-%d")
                url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={modified_date}"
            else:  # If the day is within the next 10 days then get forecast weather
                url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&dt={date}"

            response = requests.get(url)
            data = response.json()
            temperature = data['forecast']['forecastday'][0]['day']['avgtemp_c']  # Getting the average temperature for the day
            return temperature

    @property
    def date(self):  # Getter method to access the date of the day
        return self.__date

    @date.setter
    def date(self, date):  # Setter method to update the date of the day
        self.__date = date

    @property
    def day(self):  # Getter method to access the day of the week
        return self.__day

    @day.setter
    def day(self, day):  # Setter method to update the day of the week
        self.__day = day

    @property
    def city(self):  # Getter method to access the city associated with the day
        return self.__city

    @city.setter
    def city(self, city):  # Setter method to update the city associated with the day
        self.__city = city

    @property
    def activity_list(self):  # Getter method to access the list of activities
        return self.__activities

    @activity_list.setter
    def activity_list(self, activities):  # Setter method to update the list of activities
        self.__activities = activities

    def add_activity(self, name, start_hour, end_hour, city, street, post, building, apartment, ticket_needed, pdf_ticket):  # Method for adding new activity to the activity list
        localization = Localization(city, street, post, building, apartment)  # Setting the location of the activity
        activity = Activity(name, start_hour, end_hour, ticket_needed, pdf_ticket, localization)  # Setting the new activity
        self.__activities.append(activity)  # Adding a new activity to the day
        self.sort_activities()  # Sorting the activities based on start hour

    def sort_activities(self):  # Sorting activities
        self.__activities = sorted(self.__activities, key=lambda activity: activity.start_hour)

    def translate_city(self, city):  # Translating the city name from Polish to English
        translation = translate(city, "en", "pl")
        return translation

    def add_to_calendar(self, calendar):  # Adding each activity to the calendar
        for activity in self.__activities:
            activity.add_to_calendar(calendar, self.date)

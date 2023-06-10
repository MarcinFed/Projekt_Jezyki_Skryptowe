import requests
from datetime import datetime
from mtranslate import translate


class Day:
    def __init__(self, date, day, city):
        self.__date = datetime.strptime(date, "%Y-%m-%d")
        self.__day = day
        self.__city = city
        self.__activities = []
        self.__temperature = self.forecast_weather(self.__city, date)

    @property
    def temperature(self):
        return self.__temperature

    def forecast_weather(self, pl_city, date):
        api_key = "a6a41775e527476da69162248231006"
        city = self.translate_city(pl_city)

        target_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()

        if (target_date.date() - today.date()).days > 10:
            previous_year = target_date.year - 1
            modified_date = target_date.replace(year=previous_year).strftime("%Y-%m-%d")
            url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={modified_date}"
        else:
            url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&dt={date}"

        response = requests.get(url)
        data = response.json()
        print(data)
        temperature = data['forecast']['forecastday'][0]['day']['avgtemp_c']
        return temperature

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        self.__day = day

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def activity_list(self):
        return self.__activities

    @activity_list.setter
    def activity_list(self, activities):
        self.__activities = activities

    def add_activity(self, values):
        name, start_hour, end_hour, ticket_needed, pdf_ticket, localization = values

    def translate_city(self, city):
        translation = translate(city, "en", "pl")
        return translation



if __name__ == "__main__":
    day = Day("2023-06-27", 2, "Ateny")
    print(day.temperature)
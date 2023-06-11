from Backend.Plan import Plan
from Backend.Transport import Transport
from Backend.Accommodation import Accommodation
from Backend.Localization import Localization
import os
import vobject
import datetime


class Travel:
    def __init__(self, name, destination, start_date, end_date):
        self.__name = name
        self.__destination = destination
        self.__start_date = start_date
        self.__end_date = end_date
        self.__days = (end_date - start_date).days
        self.__transport_to = None
        self.__transport_from = None
        self.__accommodation = None
        self.__plan = Plan(self.__start_date, self.__end_date, self.__destination)
        self.__medium_temp = self.set_medium_temperature()

    @property
    def plan(self):
        return self.__plan

    @property
    def transport_to(self):
        return self.__transport_to

    @transport_to.setter
    def transport_to(self, values):
        transport_type, departure_time, time, ticket = values
        self.__transport_to = Transport(transport_type, departure_time, time, ticket)

    @property
    def transport_from(self):
        return self.__transport_from

    @transport_from.setter
    def transport_from(self, values):
        transport_type, departure_time, time, ticket = values
        self.__transport_from = Transport(transport_type, departure_time, time, ticket)

    @property
    def accommodation(self):
        return self.__accommodation

    @accommodation.setter
    def accommodation(self, values):
        name, city, post_code, street, building, apartment = values
        self.__accommodation = Accommodation(name, Localization(city, post_code, street, building, apartment))

    @property
    def name(self):
        return self.__name

    @property
    def destination(self):
        return self.__destination

    @property
    def start_date(self):
        return self.__start_date

    @property
    def end_date(self):
        return self.__end_date

    @property
    def days(self):
        return self.__days

    @property
    def medium_temp(self):
        return self.__medium_temp

    def set_medium_temperature(self):
        temps = []
        for day in self.__plan.days:
            temps.append(day.temperature)

        average = sum(temps)/len(temps)
        formatted_average = f"{average:.1f}"
        return formatted_average

    def add_to_calendar(self):
        calendar = vobject.iCalendar()

        travel = calendar.add("vevent")
        travel.add("summary").value = self.name
        travel.add("location").value = self.destination
        travel.add("description").value = self.accommodation.name

        start_datetime, end_datetime = self.prepare_time()

        travel.add("dtstart").value = start_datetime
        travel.add("dtend").value = end_datetime

        self.transport_to.add_to_calendar(calendar, self.start_date)
        self.transport_from.add_to_calendar(calendar, self.end_date)

        self.__plan.add_to_calendar(calendar)

        calendar_path = "Calendar\\"+self.name+".ics"

        if not os.path.exists("Calendar"):
            os.makedirs("Calendar")

        with open(calendar_path, "w", encoding='utf-8') as file:
            file.write(calendar.serialize())

    def prepare_time(self):
        to_departure_time = datetime.datetime.strptime(self.transport_to.departure_hour, "%H:%M").time()
        start_datetime = datetime.datetime.combine(self.start_date, to_departure_time)

        from_departure_time = datetime.datetime.strptime(self.transport_from.departure_hour, "%H:%M").time()
        time_offset = datetime.timedelta(hours=float(self.transport_from.time))
        end_datetime = datetime.datetime.combine(self.end_date, from_departure_time) + time_offset

        return start_datetime, end_datetime

from Backend.Activity import Activity


class Plan:
    def __init__(self, start_date, start_hour, end_date, end_hour):
        self.__start_date = start_date
        self.__start_hour = start_hour
        self.__end_date = end_date
        self.__end_hour = end_hour
        self.__days = []

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        self.__start_date = start_date

    @property
    def start_hour(self):
        return self.__start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        self.__start_hour = start_hour

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        self.__end_date = end_date

    @property
    def end_hour(self):
        return self.__end_hour

    @end_hour.setter
    def end_hour(self, end_hour):
        self.__end_hour = end_hour

    @property
    def days(self):
        return self.__days

    @days.setter
    def days(self, day, activity):
        self.__days[day].add_activity()

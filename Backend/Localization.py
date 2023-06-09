class Localization:
    def __init__(self, city, post_code, street_name, building_number=None, apartment_number=None):
        self.__city = city
        self.__post_code = post_code
        self.__street_name = street_name
        self.__building_number = building_number
        self.__apartment_number = apartment_number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def post_code(self):
        return self.__post_code

    @post_code.setter
    def post_code(self, post_code):
        self.__post_code = post_code

    @property
    def street_name(self):
        return self.__street_name

    @street_name.setter
    def street_name(self, street_name):
        self.__street_name = street_name

    @property
    def building_number(self):
        return self.__building_number

    @building_number.setter
    def building_number(self, building_number):
        self.__building_number = building_number

    @property
    def apartment_number(self):
        return self.__apartment_number

    @apartment_number.setter
    def apartment_number(self, apartment_number):
        self.__apartment_number = apartment_number

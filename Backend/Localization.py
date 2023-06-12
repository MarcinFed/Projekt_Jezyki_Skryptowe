class Localization:  # Class that stores the localization data
    def __init__(self, city, street_name, post_code=None, building_number=None, apartment_number=None):
        self.__city = city  # Initializing the city name
        self.__post_code = post_code  # Initializing the postal code (optional)
        self.__street_name = street_name  # Initializing the street name
        self.__building_number = building_number  # Initializing the building number (optional)
        self.__apartment_number = apartment_number  # Initializing the apartment number (optional)

    @property
    def city(self):  # Getter method to access the city name
        return self.__city

    @city.setter
    def city(self, city):  # Setter method to update the city name
        self.__city = city

    @property
    def post_code(self):  # Getter method to access the postal code
        return self.__post_code

    @post_code.setter
    def post_code(self, post_code):  # Setter method to update the postal code
        self.__post_code = post_code

    @property
    def street_name(self):  # Getter method to access the street name
        return self.__street_name

    @street_name.setter
    def street_name(self, street_name):  # Setter method to update the street name
        self.__street_name = street_name

    @property
    def building_number(self):  # Getter method to access the building number
        return self.__building_number

    @building_number.setter
    def building_number(self, building_number):  # Setter method to update the building number
        self.__building_number = building_number

    @property
    def apartment_number(self):  # Getter method to access the apartment number
        return self.__apartment_number

    @apartment_number.setter
    def apartment_number(self, apartment_number):  # Setter method to update the apartment number
        self.__apartment_number = apartment_number
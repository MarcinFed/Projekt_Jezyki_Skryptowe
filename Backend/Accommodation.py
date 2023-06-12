class Accommodation:  # Class that stores the accommodation data
    def __init__(self, name, localization):
        self.__name = name  # Initializing the name of the accommodation
        self.__localization = localization  # Initializing the localization object for the accommodation

    @property
    def name(self):  # Getter method to access the name of the accommodation
        return self.__name

    @name.setter
    def name(self, name):  # Setter method to update the name of the accommodation
        self.__name = name

    @property
    def localization(self):  # Getter method to access the localization object of the accommodation
        return self.__localization

    @localization.setter
    def localization(self, localization):  # Setter method to update the localization object of the accommodation
        self.__localization = localization

class Accommodation:
    def __init__(self, name, localization):
        self.__name = name
        self.__localization = localization

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def localization(self):
        return self.__localization

    @localization.setter
    def localization(self, localization):
        self.__localization = localization

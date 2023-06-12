from Backend.Travel import Travel  # Importing the Travel class from the Backend.Travel module
import pickle  # Importing the pickle module for serialization
import os  # Importing the os module for file operations


class App:  # Class that stores data about all created travels
    def __init__(self):
        self.__travels = []  # Initializing an empty list to store travel objects
        self.__filename = "Saves\\travels.plan"  # Setting the filename for saving and loading travel data

    def add_travel(self, name, destination, start_date, end_date):  # Method to add new travel to travels list
        travel = Travel(name, destination, start_date, end_date)  # Creating a new Travel object
        self.__travels.append(travel)  # Adding the travel object to the list of travels

    @property
    def travels(self):  # Getter method to access the list of travels
        return self.__travels

    def save_to_file(self):  # Method to serialize app data
        data = {  # Creating a dictionary with 'travels' as the key and the list of travels as the value
            'travels': self.__travels,
        }

        if not os.path.exists("Saves"):  # Checking if the 'Saves' directory exists, if not, creating it
            os.makedirs("Saves")

        with open(self.__filename, "wb") as file:  # Opening the file in binary mode for writing
            pickle.dump(data, file)  # Serializing the data dictionary and writing it to the file

    def load_from_file(self):  # Method to deserialize data from file
        if not os.path.exists("Saves"):  # Checking if the 'Saves' directory exists, if not, creating it
            os.makedirs("Saves")
        if not os.path.exists(self.__filename):  # Checking if the file already exists
            open(self.__filename, 'w').close()  # Creating an empty file
        else:
            with open(self.__filename, "rb") as file:  # Opening the file in binary mode for reading
                data = pickle.load(file)  # Deserializing the data from the file
            self.__travels = data['travels']  # Updating the list of travels with the loaded data

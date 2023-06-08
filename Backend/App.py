from Backend.Travel import Travel


class App:
    def __init__(self):
        self.travels = []

    def add_travel(self, name, destination, start_date, end_date):
        travel = Travel(name, destination, start_date, end_date)
        self.travels.append(travel)


if __name__ == "__main__":
    app = App()
    app.add_travel("cos","cos","cos","cos")
    print(app.travels[0])



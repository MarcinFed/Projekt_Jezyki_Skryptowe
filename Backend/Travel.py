import Plan


class Travel:
    def __init__(self, destination, start_date, end_date):
        self.destination = destination
        self.start_data = start_date
        self.end_data = end_date
        self.transport = None
        self.accommodation = None
        self.plan = None

    def make_plan(self):
        self.plan = Plan()

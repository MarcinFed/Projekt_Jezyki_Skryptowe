class Activity:
    def __init__(self, name, start_hour, end_hour, ticket_needed=False, pdf_ticket=None, localization=None):
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.ticket_needed = ticket_needed
        self.pdf_ticket = pdf_ticket
        self.localization = localization

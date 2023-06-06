class Transport:
    def __init__(self, transport_type, departure_hour, time, pdf_ticket=None):
        self.transport_type = transport_type
        self.departure_hour = departure_hour
        self.time = time
        self.pdf_ticket = pdf_ticket
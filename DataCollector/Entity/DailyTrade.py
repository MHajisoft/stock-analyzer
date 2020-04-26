class DailyTrade:
    def __init__(self, data):
        self.Code = data[0]
        self.Open = data[1]
        self.Close = data[2]
        self.High = data[3]
        self.Low = data[4]

    def __repr__(self):
        return f"Code:{self.Code} - Open:{self.Open} - Close:{self.Close} - High:{self.High} - Low:{self.Low}"

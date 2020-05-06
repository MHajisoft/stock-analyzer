class SymbolsDaily:
    def __init__(self, data,date):
        self.Id = None
        self.Code = None
        self.Date = date
        self.Namad = data[0]
        self.Count = int(data[2])
        self.Volume = int(data[3])
        self.Price = int(data[4])
        self.Yesterday = int(data[5])
        self.Open = int(data[6])
        self.Last = int(data[7])
        self.Close = int(data[10])
        self.Low = int(data[13])
        self.High = int(data[14])

    def __repr__(self):
        return self.Namad

    def props(self):
        return dict((key, getattr(self, key)) for key in dir(self) if key not in dir(self.__class__))

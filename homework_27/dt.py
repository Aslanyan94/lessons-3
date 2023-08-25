class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def add_day(self, day):
        pass

    def add_month(self, month):
        pass

    def add_year(self, year):
        pass

    def __str__(self): # day.month.year # 23.10.2020
        pass


class Time:
    def __init__(self, hours, minute, second):
        self.hours = hours
        self.minute = minute
        self.second = second

    def add_hours(self, hours):
        self.hours += hours
        days = self.hours // 24
        self.hours %= 24
        return days

    def add_minutes(self, minutes):
        self.minute += minutes
        self.add_hours(self.minute // 60)
        self.minute %= 60

    def add_seconds(self, seconds):
        self.second += seconds
        self.add_minutes(self.second // 60) # second    minute      hour
        self.second %= 60                   # 3600*25   60 * 25     25

    def __str__(self):
        return f"{self.hours}:{self.minute}:{self.second}"


class DateTime(Date, Time):
    pass

    # def __str__(self):
    #     pass # "23.12.2020 22:53:12"
# time = Time(hours=1, minute=1, second=1)
# time.add_seconds(3600 * 23)
# print(time)


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
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_hours(self, hours):
        self.hour += hours
        days = self.hour // 24
        self.hour %= 24
        return days

    def add_minutes(self, minutes):
        self.minute += minutes
        self.add_hours(self.minute // 60)
        self.minute %= 60

    def add_seconds(self, seconds):
        self.second += seconds
        self.add_minutes(self.second // 60)     # second    minute      hour
        self.second %= 60                       # 3600*25   60 * 25     25

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"


class DateTime(Date, Time):
    def __init__(self, year, month, day, hour, minute, second):
        Date.__init__(self, year, month, day)
        Time.__init__(self, hour=hour, minute=minute, second=second)

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year} {self.hour:0>2}:{self.minute:0>2}:{self.second:0>2}"


# time = Time(hours=1, minute=1, second=1)
# time.add_seconds(3600 * 23)
# print(time)
dt = DateTime(year=2023, month=11, day=25,
              hour=23, minute=3, second=54,)
print(dt)
dt.add_minutes(57)
dt.add_seconds(6)
print(dt)

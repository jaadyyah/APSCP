class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        added = Time(0, 0, 0)
        added.second = self.second + other.second
        added.minute = self.minute + other.minute
        added.hour = self.hour + other.hour
        if added.second >= 60:  # if this exceeded 60 it will start to add minutes
            added.minute += 1
            added.second -= 60
        if added.minute >= 60:  # if this exceeded 60 it will start to add hours
            added.hour += 1
            added.minute -= 60
        if added.hour >= 24:
            added.hour -= 24
        return added

    def __str__(self):
        return 'Hours: ' + str(self.hour) + ' Minutes: ' + str(self.minute) + ' Seconds: ' + str(self.second)

time = Time(15, 66, 30)
time2 = Time(5, 50, 5)
print(time + time2)

# I, Mikael Reyes, have checked that the math within the code works :D
# Hi this is Claire and the code works well, it converts seconds and minutes and it add properly

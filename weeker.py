class WeekDayError(Exception):
    pass
	

class Weeker:
    __weekDay = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        if day not in self.__weekDay:
            raise WeekDayError
        self.__index = self.__weekDay.index(day)

    def __str__(self):
        return self.__weekDay[self.__index]

    def add_days(self, n):

        for i in range(n):
            self.__index += 1
            if self.__index == 7:
                self.__index = 0

    def subtract_days(self, n):
        
        for i in range(n):
            self.__index -= 1
            if self.__index == -1:
                self.__index = 6

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")

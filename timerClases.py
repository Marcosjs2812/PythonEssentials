import time

class Timer:
    def __init__(self, hour = 0, min = 0, sec = 0):
        
        if sec not in range(0,60) or min not in range(0,60) or hour not in range(0,24): 
            raise ValueError

        self.__sec = sec
        self.__min = min
        self.__hour = hour

    def __str__(self):
        
        second = "0" + str(self.__sec) if self.__sec < 10 else str(self.__sec)
        minute = "0" + str(self.__min) if self.__min < 10 else str(self.__min)
        hourly = "0" + str(self.__hour) if self.__hour < 10 else str(self.__hour)
        
        return hourly + ":" + minute + ":" + second
        

    def next_second(self):
        if self.__sec + 1 == 60:
            self.__sec = 0
            if self.__min + 1 == 60:
                self.__min = 0
                if self.__hour + 1 == 24:
                    self.__hour = 0
                else:
                    self.__hour += 1
            else:
                self.__min += 1
        else:
            self.__sec += 1
        

    def prev_second(self):
        if self.__sec - 1 == -1:
            self.__sec = 59
            if self.__min - 1 == -1:
                self.__min = 59
                if self.__hour - 1 == -1:
                    self.__hour = 23
                else:
                    self.__hour -= 1
            else:
                self.__min -= 1
        else:
            self.__sec -= 1

timer = Timer(23, 59, 59)
sec = 0
while True:
    try:
        timer.prev_second()
        print(timer)
        time.sleep(0.1)
    except ValueError:
        print("Se ingresó una hora inválida")


# Ejemplo del curso de Cisco ###############################
# def two_digits(val):
#     s = str(val)
#     if len(s) == 1:
#         s = '0' + s
#     return s


# class Timer:
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds

#     def __str__(self):
#         return two_digits(self.__hours) + ":" + \
#                two_digits(self.__minutes) + ":" + \
#                two_digits(self.__seconds)

#     def next_second(self):
#         self.__seconds += 1
#         if self.__seconds > 59:
#             self.__seconds = 0
#             self.__minutes += 1
#             if self.__minutes > 59:
#                 self.__minutes = 0
#                 self.__hours += 1
#                 if self.__hours > 23:
#                     self.__hours = 0

#     def prev_second(self):
#         self.__seconds -= 1
#         if self.__seconds < 0:
#             self.__seconds = 59
#             self.__minutes -= 1
#             if self.__minutes < 0:
#                 self.__minutes = 59
#                 self.__hours -= 1
#                 if self.__hours < 0:
#                     self.__hours = 23


# timer = Timer(23, 59, 59)
# print(timer)
# timer.next_second()
# print(timer)
# timer.prev_second()
# print(timer)

totalEvents = 0

import calendar

class cs101events:
    __myevents = []
    __d = []
    __m = []
    __y = []

    currentEvent = 0
    minWords = 2
    maxWords = 20

    
    def __init__(self):

        global totalEvents
        totalEvents += 2

    def getNextEvent(self):

        nextEvent = self.__myevents[self.currentEvent]
        nextEventDay = self.__d[self.currentEvent]
        nextEventMonth = self.__m[self.currentEvent]
        nextEventYear = self.__y[self.currentEvent]
        
        self.currentEvent += 1
        if (self.currentEvent >= len(self.__myevents)):
            self.currentEvent = 0
        
        def dateToWeek():
            weekDayInt = calendar.weekday(int(nextEventYear), int(nextEventMonth), int(nextEventDay))
            
            if(weekDayInt == 0):
                return "Monday"
            elif(weekDayInt == 1):
                return "Tuesday"
            elif(weekDayInt == 2):
                return "Wednesday"
            elif(weekDayInt == 3):
                return "Thursday"
            elif(weekDayInt == 4):
                return "Friday"
            elif(weekDayInt == 5):
                return "Saturday"
            elif(weekDayInt == 6):
                return "Sunday"
            else:
                return "Something went wrong while converting a date to a weekday."

        weekDay = dateToWeek()
        
        print(calendar.weekday(int(nextEventYear), int(nextEventMonth), int(nextEventDay)))
        print(type(calendar.weekday(int(nextEventYear), int(nextEventMonth), int(nextEventDay))))
        
        return(nextEvent+" on "+ weekDay +" " +nextEventDay+"-"+nextEventMonth+"-"+nextEventYear)
    

    def addNewEvent(self, event, d, m, y):
        self.__myevents.append(event)
        self.__d.append(d)
        self.__m.append(m)
        self.__y.append(y)

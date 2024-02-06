class Player:
    def __init__ (self):
        self.fname = "FNAME"
        self.lname = "LNAME"
        self.number = 00
        self.gradYear = 0000
        self.isPitcher = False
        self.isHitter = False
        self.statistics = []
    def __init__(self, fname, lname, number, gradYear, isPitcher, isHitter):
        self.fname = fname
        self.lname = lname
        self.number = number
        self.gradYear = gradYear
        self.isPitcher = isPitcher
        self.isHitter = isHitter
        self.statistics = []
    def addStatistic(self,stat):
        self.statistics.append(stat)
    def printPerson(self):
        print("************")
        print("PLAYER: ", self.fname, " ", self.lname)
        print("#",self.number, "\tGraduation Year: ",self.gradYear)
        if(self.isPitcher and not self.isHitter):
            print("Pitcher Only")
        elif(not self.isPitcher and self.isHitter):
            print("Position Player")
        elif(self.isHitter and self.isPitcher):
            print("2-Way Player")
        print()
        print("STATISTICS")
        for i in range(len(self.statistics)):
            print(self.statistics[i])
        print("************")
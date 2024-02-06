import DataProcessor
import Player
import Statistic

lj = Player("Luke","Johnson",10,2024,True,False)
strikeouts = Statistic("AVG",0.333)
lj.addStatistic(strikeouts)
lj.printPerson()
print(DataProcessor.normOf(lj.statistics)**2)
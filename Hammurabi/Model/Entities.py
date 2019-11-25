class City:

    def __init__(self,year,starvedPeople,newpeople,population,acres,harvest,rats,landPrice,grainStocks):
        self.__landPrice = landPrice
        self.__rats = rats
        self.__harvest = harvest
        self.__population = population
        self.__newpeople = newpeople
        self.__starvedPeople = starvedPeople
        self.__year = year
        self.__acres = acres
        self.__grainStocks = grainStocks

    def getAcres(self):
        return self.__acres

    def getGrainStocks(self):
        return self.__grainStocks

    def getYear(self):
        return self.__year

    def getStarved(self):
        return self.__starvedPeople

    def getNewPeople(self):
        return self.__newpeople

    def getPopulation(self):
        return self.__population

    def getHarvest(self):
        return self.__harvest

    def getRats(self):
        return self.__rats

    def getLandPrice(self):
        return self.__landPrice

    def setAcres(self,newAcres):
        self.__acres=newAcres

    def setGrainStocks(self,newGrainStocks):
        self.__grainStocks=newGrainStocks

    def setYear(self,newYear):
        self.__year=newYear

    def setLandPrice(self,newLandPrice):
        self.__landPrice=newLandPrice

    def setRats(self,newRats):
        self.__rats=newRats

    def setHarvest(self,newHarvest):
        self.__harvest=newHarvest

    def setPopulation(self,newPopulation):
        self.__population=newPopulation

    def setNewPeople(self,new):
        self.__newpeople=new

    def setStarved(self,newStarved):
        self.__starvedPeople=newStarved



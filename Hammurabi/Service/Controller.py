from random import randint


class ServiceGame():

    def __init__(self,ctrlPlayer):
        self.ctrlPlayer = ctrlPlayer

    def updateHarvestUnit(self):
        harvestUnit=randint(1,6)
        self.ctrlPlayer.city.setHarvest(harvestUnit)

    def updateAcresPrice(self):
        acresPrice=randint(15,25)
        self.ctrlPlayer.city.setLandPrice(acresPrice)

    def ratsInfestation(self):
        chance=randint(1,5)
        if chance == 5:
            grainStocks=self.ctrlPlayer.city.getGrainStocks()
            rats=grainStocks*0.1
            grainStocks=grainStocks-rats
            if grainStocks < 0:
                grainStocks=0
            self.ctrlPlayer.city.setRats(rats)
            self.ctrlPlayer.city.setGrainStocks(grainStocks)
        else:
            self.ctrlPlayer.city.setRats(0)

    def newPeople(self):
        starved=self.ctrlPlayer.city.getStarved()
        if starved == 0:
            incomingPeople=randint(0,10)
            oldPopulation=self.ctrlPlayer.city.getPopulation()
            newPopulation=oldPopulation+incomingPeople
            self.ctrlPlayer.city.setPopulation(newPopulation)
            self.ctrlPlayer.city.setNewPeople(incomingPeople)
        else:
            self.ctrlPlayer.city.setNewPeople(0)

    def halfPopulationStarved(self):
        population=self.ctrlPlayer.city.getPopulation()
        starved=self.ctrlPlayer.city.getStarved()
        halfpopulation=population//2
        if starved >= halfpopulation:
            return 1
        else:
            return 0

    def checkStats(self):
        population=self.ctrlPlayer.city.getPopulation()
        acres=self.ctrlPlayer.city.getAcres()
        if population > 100 and acres > 1000:
            return 1
        else:
            return 0

class ServicePlayer():

    def __init__(self,city,valid):
        self.valid = valid
        self.city = city

    def decision(self,answer):
        if answer > 0:
            acresPrice=self.city.getLandPrice()
            amountOfGrain=answer*acresPrice

            oldAmountOfGrain=self.city.getGrainStocks()
            self.valid.validBuyAcres(oldAmountOfGrain,amountOfGrain)

            oldacres=self.city.getAcres()
            newacres=oldacres+answer
            self.city.setAcres(newacres)

            oldGrain=self.city.getGrainStocks()
            newGrain=oldGrain-amountOfGrain
            self.city.setGrainStocks(newGrain)
        elif answer < 0:
            amountOfAcres=self.city.getAcres()
            self.valid.validSellAcres(amountOfAcres,answer)

            newAmountOfAcres=amountOfAcres+answer
            self.city.setAcres(newAmountOfAcres)

            acresPrice=self.city.getLandPrice()
            stockOfGrain=self.city.getGrainStocks()
            newStockOfGrain=stockOfGrain-(answer*acresPrice)
            self.city.setGrainStocks(newStockOfGrain)


    def feedPopulation(self,grain):

        oldAmountOfGrain=self.city.getGrainStocks()
        self.valid.validGrainToPopulation(oldAmountOfGrain,grain)

        newAmountOfGrain=oldAmountOfGrain-grain
        self.city.setGrainStocks(newAmountOfGrain)

        self.StarvedPopulation(grain)

    def acresToPlant(self,acres):
        amountOfAcres=self.city.getAcres()
        self.valid.validPlantAcresAcres(amountOfAcres,acres)

        amountOfGrain=self.city.getGrainStocks()
        self.valid.validPlantAcresGrain(amountOfGrain,acres)

        harvest=self.city.getHarvest()
        amountHarvest=harvest*acres

        people=self.city.getPopulation()
        maxHarvestAcres=people*10
        peopleHarvest=harvest*maxHarvestAcres

        if peopleHarvest < amountHarvest:
            amountHarvest=peopleHarvest

        self.city.setGrainStocks(amountHarvest)

    def StarvedPopulation(self, grain):
        peopleFed=grain//20
        population=self.city.getPopulation()
        starvingPeople=population-peopleFed
        self.city.setStarved(starvingPeople)
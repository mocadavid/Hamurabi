from NewExceptions.NewErrors import BuyAcresExcept, SellAcresExcept, FeedPopulationExcept, InvalidAmountOfGrain, \
    InvalidAmountOfAcres, PlantAcresExcept, PlantAcresExceptGrain


class ValidCity:

    def validBuyAcres(self,oldAmountOfGrain,amountOfGrain):
        if oldAmountOfGrain < amountOfGrain:
            raise BuyAcresExcept("Too few grain!")

    def validSellAcres(self,old,amount):
        if old < amount:
            raise SellAcresExcept("Too few acres!")

    def validGrainToPopulation(self,old,amount):
        if amount < 0:
            raise InvalidAmountOfGrain("Invalid grain format!")
        if old < amount:
            raise FeedPopulationExcept("Too few grain!")

    def validPlantAcresAcres(self,old,amount):
        if amount < 0:
            raise InvalidAmountOfAcres("Invalid acres format!")
        if old < amount:
            raise PlantAcresExcept("Too few acres!")

    def validPlantAcresGrain(self,old,amount):
        if old < amount:
            raise PlantAcresExceptGrain("Too few grain!")
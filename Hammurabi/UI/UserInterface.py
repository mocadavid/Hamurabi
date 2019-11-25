from NewExceptions.NewErrors import BuyAcresExcept, SellAcresExcept, FeedPopulationExcept, InvalidAmountOfGrain, \
    InvalidAmountOfAcres, PlantAcresExcept, PlantAcresExceptGrain


class Console:

    def __init__(self,servicePlayer,serviceGame):
        self.serviceGame = serviceGame
        self.servicePlayer = servicePlayer

    def startGameUI(self):
        newYear=self.servicePlayer.city.getYear()
        while newYear<=5:
            self.advisorReportUI()
            self.serviceGame.updateHarvestUnit()
            self.decisionUI()
            self.serviceGame.updateAcresPrice()
            self.serviceGame.ratsInfestation()
            self.serviceGame.newPeople()
            if self.serviceGame.halfPopulationStarved():
                break
            newYear+=1
            self.servicePlayer.city.setYear(newYear)
        self.TheEndUI()

    def advisorReportUI(self):
        year=self.servicePlayer.city.getYear()
        starved=self.servicePlayer.city.getStarved()
        print("In year",year,starved," people starved")
        newPeople=self.servicePlayer.city.getNewPeople()
        print(newPeople,"people came to the city.")
        population=self.servicePlayer.city.getPopulation()
        print("City population is",population)
        acres=self.servicePlayer.city.getAcres()
        print("City owns",acres,"acres of land.")
        harvest=self.servicePlayer.city.getHarvest()
        print("Harvest was ",harvest,"units per acre")
        rats=self.servicePlayer.city.getRats()
        print("Rats ate",rats,"units")
        landprice=self.servicePlayer.city.getLandPrice()
        print("Land price is",landprice,"units per acre")
        grainStocks=self.servicePlayer.city.getGrainStocks()
        print("\nGrain stocks are",grainStocks,"units.")

    def decisionUI(self):
        while True:
            print("Acres to buy/sell(+/-)")
            try:
                answer1=int(input("->"))
                self.servicePlayer.decision(answer1)
                break
            except ValueError as ve:
                print(ve)
            except BuyAcresExcept as be:
                print(be)
            except SellAcresExcept as se:
                print(se)
        while True:
            print("Units to feed the population")
            try:
                answer2 = int(input("->"))
                self.servicePlayer.feedPopulation(answer2)
                break
            except ValueError as ve:
                print(ve)
            except FeedPopulationExcept as fe:
                print(fe)
            except InvalidAmountOfGrain as ig:
                print(ig)

        while True:
            print("Acres to plant")
            try:
                answer3 = int(input("->"))
                self.servicePlayer.acresToPlant(answer3)
                break
            except ValueError as ve:
                print(ve)
            except InvalidAmountOfAcres as ia:
                print(ia)
            except PlantAcresExcept as pe:
                print(pe)
            except PlantAcresExceptGrain as pg:
                print(pg)

    def TheEndUI(self):
        if self.serviceGame.checkStats():
            print("You Won!")
        else:
            print("Game over! U lose!")
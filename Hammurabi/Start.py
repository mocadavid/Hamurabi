

from Model.Entities import City
from Service.Controller import ServicePlayer, ServiceGame
from UI.UserInterface import Console
from Validation.Validator import ValidCity

city=City(1,0,0,100,1000,3,200,20,2800)
validCity=ValidCity()
servicePlayer=ServicePlayer(city,validCity)
serviceGame=ServiceGame(servicePlayer)
console=Console(servicePlayer,serviceGame)

console.startGameUI()

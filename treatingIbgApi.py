import requests
import json
import removeAccents


class CitiesFromBrazil():

    def __init__(self):
        pass

    def getBrazilStates(self):
        brazil = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/distritos')
        return brazil.json()

    def filteringStatesData(self):
        brazil = self.getBrazilStates()
        newBrazilObj = []
        
        # didn't had time to take a look at a better complexity execution solution
        for states in brazil:
            state = states['municipio']['microrregiao']['mesorregiao']['UF']['sigla']
            cities = []
            counter = 0

            for county in brazil:
                cityUf = county['municipio']['microrregiao']['mesorregiao']['UF']['sigla']
                cityData = county['municipio']
                if cityUf == state:
                    cities.append( { 'id': cityData['id'], 'city': self.accentsRemover(cityData['nome'])} )
            
            counter += 1
            newBrazilObj.append( { 'id': counter, state: cities, 'country': 'Brazil' } )

        return newBrazilObj
    
    def writeJsonFile(self):
        with open('brazil.json', 'w', encoding = 'utf-8') as outputFile:
            return json.dump(self.filteringStatesData(), outputFile)
    
    def accentsRemover(self, text):
        cleanText = str()
        for letter in text:
            cleanText += removeAccents.removeAccents(letter)
        
        return cleanText

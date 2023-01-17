class Country:
    def __init__(self, name: str, population: int, capital: str):
        self.name = name
        self.population = population
        self.capital = capital
    
    def increase_population(self, num: int):
        return self.population * num

    def add (self, other):
        self.name = self.name + ' ' + other.name
        self.population = self.population + other.population
        return Country (self.name, self.population)

    def __add__(self, val2): 
        return Country(self.name + " " + val2.name, self.population+val2.population) 
  
    


japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
print(japan.increase_population(2))


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
bosnia_herzegovina = bosnia.add(herzegovina)


#custom class
#class: a data type that holds information, used for object oriented programming 
#create swimmer class (four event meet) for now
#class names start with uppercase letter 

class Swimmer:
    #self refers to whatever swimmer we want to analyze 
    #__init__ function initializes the class 
    #first argument in a class method is self 
    #function in a class is called a method 
    #self is person before the dot 
    def __init__(self, name, time) -> None:
        self.name = name
        self.time = time 
    def compare(self, swimmer2):
        if self.time < swimmer2.time:
            winner = self
        else:
            winner = swimmer2 
        print(f'winner:, {winner.name}')
        return winner == self

carlie = Swimmer("Carlie", 56.00)
print(carlie)
print(carlie.name)
print(carlie.time)

#calling the __init__ function
#words need to be in quotes, numbers do not
sydney = Swimmer("Sydney", 52.31)

print(sydney)
print(sydney.name)
print(sydney.time)

print("-----")

print(carlie.compare(sydney))

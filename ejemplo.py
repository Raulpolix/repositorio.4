class Animal
    def __init__(self,species,message):
        self.species = species
        self.stamina = 0
        self.message = message

    def speak(self):
      return message


class Dog(Animal):
    def speak(self):
        return translate('dog_language',self.message)

dog = Dog('dog','Guau guau')

    

# Method overriding 
# A simple demo of subclass overriding an already defined method in parent class


# superclass Animal
class Animal:
    def __init__(self, sound, locomotion, sex, legs):
        self.sound = sound
        self.locomotion = locomotion
        self.sex = sex
        self.legs = legs
        

    def locomotion_type(self):
        return f"Animal locomotion type is {self.locomotion}"
    def speak(self):
        return f"The sound this animal makes is {self.sound}"
    
# Subclass dog inherits all methods in superclass Animal but the speak method is defined again in subclass dog  
class dog(Animal):
    def speak(self):
        print("woof")
        return super().speak()
# this method uses super to return the method from superclass after fufilling the redefined method

Bingo = dog("Bark", "walk", "male", 4)

# here the when locomotion type is printed, it follows the defined method in superclass Animal, but when Speak is printed it follow the
# defined method in subclass. And that is overriding!
print(Bingo.locomotion_type())
print(Bingo.speak())



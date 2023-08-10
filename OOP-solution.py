# Define base Podracer class
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"

# Child class of Podracer    
class AnakinsPod(Podracer):
  def boost(self):
    self.max_speed *= 2
    
# Another child class  
class SebulbasPod(Podracer):
  def flame_jet(self, other):
    other.condition = "trashed"



    #How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    #Inheritance:
    #The child classes AnakinsPod and SebulbasPod inherit from the parent Podracer class.       
    
    #Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    # For this particular problem of modeling podracers and their behaviors, an object-oriented approach makes the most sense and would likely be easier than other coding styles.

    #How in particular did Object Oriented Programming assist in the solving of this problem?
    #It allowed modeling the real-world domain (podracers) more directly using objects and classes. This created an intuitive mapping from problem to code.
   

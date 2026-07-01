#parent class

class Dietplan:
    def get_breakfast(self):
        #base method to be overridden by child class
        pass

#child class 1 : keto diet plan
class KetoDiet(Dietplan):
    def get_breakfast(self):
        return ("Eggs", "Avocado", "Bacon")

#child class 2 : vegan diet plan
class VeganDiet(Dietplan):
    def get_breakfast(self):
        return ("Oatmeal with milk", "Chia seeds")

#child class 3 : high protien diet plan
class HighProteinDiet(Dietplan):
    def get_breakfast(self):
        return ("Protein smoothie", "Greek yogurt", "Berries")

#polymorphism function
#this function accept any diet object and call its 'get_breakfast' method
def print_breakfast(diet):
    print(f"Today's breakfast: {', '.join(diet.get_breakfast())}")

#create a instance
keto_diet = KetoDiet()
vegan_diet = VeganDiet()
high_protein_diet = HighProteinDiet()

#pass the difference objects into the exact same function
print_breakfast(keto_diet)          # Output: Today's breakfast: Eggs, Avocado, Bacon
print_breakfast(vegan_diet)         # Output: Today's breakfast: Oatmeal with milk, Chia seeds
print_breakfast(high_protein_diet)  # Output: Today's breakfast: Protein smoothie, Greek yogurt, Berries
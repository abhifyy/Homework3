"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, servings=1.0):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


try:
    food_name = input()
    fat_grams = float(input())
    carbs_grams = float(input())
    protein_grams = float(input())
    num_servings = float(input())

    food_item_default = FoodItem()
    food_item_default.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item_default.get_calories(num_servings)))
    print()

    food_item_input = FoodItem(food_name, fat_grams, carbs_grams, protein_grams)
    food_item_input.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item_input.get_calories(num_servings)))


except (ValueError, EOFError):
    print()
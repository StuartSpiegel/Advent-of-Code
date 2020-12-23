# --- Day 21: Allergen Assessment --- You reach the train's last stop and the closest you can get to your vacation
# island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You
# just need a few days' worth of food for your journey.
#
# You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are
# listed in a language you do understand. You should be able to use this information to determine which ingredient
# contains which allergen and work out which foods are safe to take with you on your trip.
#
# You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's
# ingredients list followed by some or all of the allergens the food contains.
#
# Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't
# always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient
# that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an
# allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to
# label it, or maybe it was labeled in a language you don't know.
#
# For example, consider the following list of foods:
#
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish) trh fvjkl sbzzf mxmxvkd (contains dairy) sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish) The first food in the list has four ingredients (written in a language you
# don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens
# the food definitely contains are listed afterward: dairy and fish.
#
# The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your
# list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting
# the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each
# except sbzzf, which appears twice.
#
# Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of
# those ingredients appear?


file = open('input.txt')
labels = [e.replace(")", "").split(" (contains ") for e in file.read().split("\n")]

allergens = {}
# Create a dict with the possible ingredients for each allergen:
# {'dairy': ['mxmxvkd'], 'fish': ['sqjhc', 'mxmxvkd'], 'soy': ['sqjhc', 'fvjkl']}
occurrences = {}
# Count how many times each ingredient appears
# {'mxmxvkd': 3, 'kfcds': 1, 'sqjhc': 3, 'nhms': 1, 'trh': 1, 'fvjkl': 2, 'sbzzf': 2}
for label in labels:
    for allergen in label[1].split(', '):
        if allergen in allergens:
            allergens[allergen] = [i for i in label[0].split(' ') if i in allergens[allergen]]
        else:
            allergens[allergen] = [i for i in label[0].split(' ')]
    for ingredient in label[0].split(' '):
        if ingredient in occurrences:
            occurrences[ingredient] += 1
        else:
            occurrences[ingredient] = 1

# Count how many time an ingredient is not possible in an allergen use occurrences to keep track of times.
count = 0
for ingredient, times in occurrences.items():
    if all(ingredient not in v for v in allergens.values()):
        count += times

# Remove the allergens that are unique
used = set()
while any(len(a) > 1 for a in allergens.values()):
    for allergen, ingredient in allergens.items():
        if len(ingredient) == 1 and ingredient[0] not in used:
            used.add(ingredient[0])
        elif len(ingredient) > 1:
            for i in used:
                if i in ingredient:
                    allergens[allergen].remove(i)

# Sort allergens alphabetically and add ingredient to string.
ingredients = ','.join(v[0] for k, v in sorted(allergens.items(), key=lambda k: k[0]))

print(f"Part One: {count}")
print(f"Part Two: {ingredients}")

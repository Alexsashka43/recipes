def recipe_dict():
    with open('recipes.txt', 'r', encoding='utf-8') as recipes:
        cook_book = {}
        def recipe_dict():
            dishes = recipes.readline().strip()
            if dishes:
                cook_book[dishes] = []
                ingredients = recipes.readline()
                for line in range(int(ingredients)):
                    ingredient = recipes.readline().strip().split(' | ')
                    ingredient_dictionary = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                    cook_book[dishes].append(ingredient_dictionary)
            else:
                return(cook_book)
            recipes.readline()
            recipe_dict()
        recipe_dict()
    return(cook_book)
recipe_dict()

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = recipe_dict()
    shoplist = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredients in cook_book[dish_name]:
                if ingredients['ingredient_name'] in shoplist:
                    shoplist[ingredients['ingredient_name']]['quantity'] += int((ingredients['quantity']) * person_count)
                else:
                    shoplist[ingredients['ingredient_name']] = {'measure': ingredients['measure'], 'quantity': int(ingredients['quantity']) * person_count}
        else:
            print('Такого блюда нет')
    return shoplist
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def read_recipe_file(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            recipe_name = lines[i].strip()
            i += 1

            # Проверяем, что текущая строка содержит числовое значение
            if i < len(lines) and lines[i].strip().isdigit():
                num_ingredients = int(lines[i].strip())
                i += 1
            else:
                # В случае, если следующая строка не является числом, пропускаем этот шаг
                continue

            ingredients = []
            for _ in range(num_ingredients):
                ingredient_info = lines[i].strip().split('|')
                ingredient = {
                    'ingredient_name': ingredient_info[0].strip(),
                    'quantity': int(ingredient_info[1].strip()),
                    'measure': ingredient_info[2].strip()
                }
                ingredients.append(ingredient)
                i += 1
            cook_book[recipe_name] = ingredients
            i += 1
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

def print_shop_list(shop_list):
    for ingredient, info in shop_list.items():
        print(f"{ingredient}: {info['quantity']} {info['measure']}")

if __name__ == "__main__":
    file_path = 'C:/Users/hake1/PycharmProjects/recept/recipes.txt'  # Укажите путь к вашему файлу
    cook_book = read_recipe_file(file_path)

    dishes_to_cook = ['Рис с овощами', 'Салат Цезарь']
    person_count = 2
    shop_list = get_shop_list_by_dishes(dishes_to_cook, person_count)

    print_shop_list(shop_list)



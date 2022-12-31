# optional_params.py

shopping_list = {}

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_items(shopping_list, *item_names):
    for item_name in item_names:
        shopping_list[item_name] = 1

    return shopping_list

shopping_list = add_items(shopping_list, "Coffee", "Tea", "Cake", "Bread")
show_list(shopping_list)
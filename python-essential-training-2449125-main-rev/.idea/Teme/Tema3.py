# optional_params.py

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name, quantity, shopping_list=None):
    if shopping_list is None:
        shopping_list = {}
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

    return shopping_list

clothes_shop_list = add_item("Shirt", 3)
electronics_store_list = add_item("USB cable", 1)
show_list(clothes_shop_list)
show_list(electronics_store_list)
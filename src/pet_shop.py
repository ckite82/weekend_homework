# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(dictionary):
    return dictionary["name"]

def get_total_cash(dictionary):
    return dictionary["admin"]["total_cash"]

def add_or_remove_cash(dictionary, cash):
    dictionary["admin"]["total_cash"] += 10
    return get_total_cash
    
def add_or_remove_cash(dictionary, cash):
    dictionary["admin"]["total_cash"] -= 10
    return get_total_cash

def get_pets_sold(dictionary):
    return dictionary["admin"]["pets_sold"]

def increase_pets_sold(dictionary, sales):
    dictionary["admin"]["pets_sold"] += 2
    return get_pets_sold

def get_stock_count(dictionary):
    return len(dictionary["pets"])

def get_pets_by_breed(pet_shop_info, breed_type):
    breed_list = []
    for pet in pet_shop_info["pets"]:
        if pet["breed"] == breed_type:
            breed_list.append(pet["breed"])
    return breed_list
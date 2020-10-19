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
# cannot get both functions to run as the first seems to affect the total when trying to run the second, how do i amend them so that they can run simaltaneously.
# for a long time it was giving me a syntax error against += condition

def get_pets_sold(dictionary):
    return dictionary["admin"]["pets_sold"]

def increase_pets_sold(dictionary, sales):
    dictionary["admin"]["pets_sold"] += 2
    return get_pets_sold

def get_stock_count(dictionary):
    return len(dictionary["pets"])

def get_pets_by_breed(dictionary, breed_type):
    breed_list = []
    for pet in dictionary["pets"]:
        if pet["breed"] == breed_type:
            breed_list.append(pet["breed"])
    return breed_list
# my first attemp at this wasn;t far off the mark, just needed to refer to others on slack to fine tune it,

def get_pets_by_breed(dictionary, breed_type):
    dalmations = []
    for pet in dictionary["pets"]:
        if pet["breed"] == breed_type:
            dalmations.append(pet["breed"])
    return dalmations

def find_pet_by_name(dictionary, pet_name):
    for pet in dictionary["pets"]:
        if pet["name"] == pet_name:
            return pet

# why did this need a loop, and couldn't just be called same as the early functions i.e get_pet_shop_name
# also i wanted my final return statement to be pet_name, how do i rearrange the function to end that way, e.g
# def find_pet_by_name(dictionary, pet_name):
#     for pet in dictionary["pets"]:
#         if pet_name == pet["name"]:
#             return pet_name

def find_pet_by_name(dictionary, pet_name):
    for pet in dictionary["pets"]:
        if pet["name"] == pet_name:
            return pet

# so basically the loop is doing the same as previous, but as it is not able to find the pet named "Fred", it defaults with None?

def remove_pet_by_name(dictionary, pet_remove):
    for pet in dictionary["pets"]:
        if pet["name"] == pet_remove:
            dictionary["pets"].remove(pet)


# def remove_pet_by_name(pets, name):
#     pass
#     for pet in pets["pets"]:
#         if pet["name"] == name:
#             
#             pet.pop(name)
# WRITE YOUR FUNCTIONS HERE

# test 1 - fairly straight forward, just took a short while for brain to function and 
# the test program was asking us to do. Confusing going between the two programs and
# breaking it all down, whilst trying to link everything.
def get_pet_shop_name(dictionary):
    return dictionary["name"]

# test 2 - same as above but with different key
def get_total_cash(dictionary):
    return dictionary["admin"]["total_cash"]

# test 3 tried and failed with first few attempts. I think I was on the right lines,
# but had the lay-out slightly wrong each time.
# 1. def get_total_cash(dictionary, cash):
#       return add_or_remove_cash = dictionary["admin"]["total_cash"] += cash
# 2. def add_or_remove_cash(dictionary, cash):
#       remove_cash = dictionary["admin"]["total_cash"] += cash
#       return remove_cash
# for a long time it was giving me a syntax error against += condition 
def add_or_remove_cash(dictionary, cash):
    dictionary["admin"]["total_cash"] += cash
    return get_total_cash
    
# test 4 was same as above but subtracting, the issue i had here was I cannot get
# both functions to run simaltaneously as the first seems to affect the total when
# trying to run the second, how do i amend them so that they can both run.
# def add_or_remove_cash(dictionary, cash):
#     dictionary["admin"]["total_cash"] -= cash
#     return get_total_cash

# test 5 was straight forward, similar to test 1 & 2, but with different dict keywords
def get_pets_sold(dictionary):
    return dictionary["admin"]["pets_sold"]

# test 6 was straight forward and was similar to test 3 & 4, need to get out of the habit
# of using the integer value after += and remember to use my placeholder - sales in this case.
def increase_pets_sold(dictionary, sales):
    dictionary["admin"]["pets_sold"] += sales
    return get_pets_sold

# test 7 this one was actually okay.  Also had a go at re-writing it today and got it 
# right straight-away.
def get_stock_count(dictionary):
    return len(dictionary["pets"])

# test 8 my first attemp at this wasn;t far off the mark, just needed to refer to 
# others on slack to fine tune it,
def get_pets_by_breed(dictionary, breed_type):
    breed_list = []
    for pet in dictionary["pets"]:
        if pet["breed"] == breed_type:
            breed_list.append(pet["breed"])
    return breed_list

# test 9 
def get_pets_by_breed(dictionary, breed_type):
    dalmations = []
    for pet in dictionary["pets"]:
        if pet["breed"] == breed_type:
            dalmations.append(pet["breed"])
    return dalmations

#10 why did this need a loop, and couldn't just be called 
# same as the early functions i.e get_pet_shop_name
# also i wanted my final return statement to be pet_name, 
# how do i rearrange the function to end that way, e.g
def find_pet_by_name(dictionary, pet_name):
    for pet in dictionary["pets"]:
        if pet["name"] == pet_name:
            return pet

#11 so basically the loop is doing the same as previous, but 
# as it is not able to find the pet named "Fred", it defaults
# with None?
def find_pet_by_name(dictionary, pet_name):
    for pet in dictionary["pets"]:
        if pet["name"] == pet_name:
            return pet

#12 found it hard to put the combo of words in right working order
def remove_pet_by_name(dictionary, pet_remove):
    for pet in dictionary["pets"]:
        if pet["name"] == pet_remove:
            dictionary["pets"].remove(pet)

# 13 referred to the example John ran through on Friday in the recap.
# Wasn't sure if I was accessing the new_pet dictionary properly
# before adding to the "pets" dictionary, or not. Ran the test
# and it accepted so moved on.
def add_pet_to_stock(dictionary, new_pet):
    dictionary["pets"].append(new_pet)

#14
def get_customer_cash(dictionary):
    return dictionary["cash"]

#15 # the way the test is worded and set out I thought 
# I might need to over complicate this one, was surprised 
# that an easy solution like the early tests was able to make this pass.
def remove_customer_cash(dictionary, cash):
    dictionary["cash"] -= 100
    return remove_customer_cash

#16
def get_customer_pet_count(customer):
    return len(customer["pets"])

#17
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
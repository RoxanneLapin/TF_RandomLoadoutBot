import random
from data_getter import *

def generate_loadout() -> list:

    classes_info = get_data_class("data/base_de_donnee.db")
    
    selected_class = random.choice(classes_info)[1]

    weapons_info = get_data_for_class("data/base_de_donnee.db","weapon",selected_class)

    selected_weapon = random.choice(weapons_info)[1]

    gadgets_info  = get_data_for_class("data/base_de_donnee.db","gadget",selected_class)

    selected_gadgets = random.sample(gadgets_info, k=3)


    specialization_info = get_data_for_class("data/base_de_donnee.db","specialization",selected_class)

    selected_specialization = random.choice(specialization_info)[1]



 


    loadout = [selected_class,selected_specialization,selected_weapon,selected_gadgets]
    
    return loadout

if __name__ == '__main__':
    print(generate_loadout())
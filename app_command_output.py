import randomizer


def random_loadout_output(selected_class):
    
    loadout = randomizer.generate_loadout(selected_class)
    description_embed = f"**Class**: {loadout[0]}\n" \
                        f"**Specialization**: {loadout[1]}\n" \
                        f"**Weapon**: {loadout[2]}\n" \
                        f"\n"\
                        f"**Gadget 1**: {loadout[3][0][1]}\n" \
                        f"**Gadget 2**: {loadout[3][1][1]}\n" \
                        f"**Gadget 3**: {loadout[3][2][1]}\n"
    print(description_embed)
    return description_embed
                        
    

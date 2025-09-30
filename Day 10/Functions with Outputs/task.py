def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formmated_l_name = l_name.title()

    return f"{formatted_f_name} {formmated_l_name}"



formated = format_name("Angela", "Yu")
print(formated)
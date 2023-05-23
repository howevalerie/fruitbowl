def get_string(message):
    my_string = str(input(message)).capitalize()
    return my_string

def get_integer(message):
    my_integer = int(input(message))
    return my_integer

def get_index(L, item):
    i = 0
    for x in L:
        if item in x:
            return i
        i +=1

def review_fruit(L):
    for i in range (0, len(L)):
        output = "{:20}: {:<4}".format(L[i][0], L[i][1])
        print(output)
    print("."*120)

def find_fruit(L):
    running = True
    while running == True:
        fruit_to_find = get_string("What fruit would you like to find? ").capitalize()
        if any(fruit_to_find in nested_list for nested_list in L):
            fruit_to_find_index = get_index(L, fruit_to_find)
            fruit_to_find_quantity = L[fruit_to_find_index][1]
            existing_output = "There are {} {} in the fruitbowl".format(fruit_to_find_quantity, fruit_to_find)
            print(existing_output)
            print("."*120)
            running = False
        else:
            nonexisting_output = "There are no {} in the fruitbowl. Please try again.".format(fruit_to_find)
            print(nonexisting_output)

def add_new_fruit_type(L):
    new_fruit_type = get_string("Enter new fruit type: ")
    new_fruit_quantity = get_integer("Enter quantity of new fruit type: ")
    new_list_item = [new_fruit_type, new_fruit_quantity]
    L.append(new_list_item)
    print("." * 120)
    output = "{} {} have been added to the fruitbowl. Select 'Review Fruit' on menu to see changes".format(new_fruit_quantity, new_fruit_type)
    print(output)
    print("."*120)

def remove_fruit(L):
    fruit_to_remove = get_string("What type of fruit was consumed? ")
    if any(fruit_to_remove in nested_list for nested_list in L):
        number_fruit_removed = get_integer("How many {} were consumed? ".format(fruit_to_remove))
        first_index = get_index(L, fruit_to_remove)
        original_quantity = L[first_index][1]
        new_quantity = original_quantity - number_fruit_removed
        L[first_index][1] = new_quantity
        existing_output = "{} {} have been removed from the fruitbowl. Select 'Review Fruit' on menu to see changes.".format(number_fruit_removed, fruit_to_remove)
        print(existing_output)
        print("."*120)
    else:
        nonexisting_output = "There are no {} in the fruitbowl and so they cannot be removed".format(fruit_to_remove)
        print(nonexisting_output)
        print("."*120)

def update_fruit(L):
    entity_options = """
    What would you like to update?
    A: Fruit Name
    B: Fruit Quantity
    """

    running = True
    going = True
    while running == True:
        fruit_to_update = get_string("What fruit would you like to update? ")
        if any(fruit_to_update in nested_list for nested_list in L):
            fruit_index = get_index(L, fruit_to_update)
            print(entity_options)

            while going == True:
                update_entity = get_string("Enter the corresponding letter of the entity you would like to update: ")
                if update_entity == "A":
                    original_name = L[fruit_index][0]
                    new_name = get_string("What would you like to update '" + original_name + "' to? ")
                    L[fruit_index][0] = new_name
                    output = "'{}' has been updated to '{}'. Select 'Review Fruit' on menu to see changes.".format(original_name, new_name)
                    print(output)
                    print("." * 120)
                    going = False
                    running = False
                elif update_entity == "B":
                    original_quantity = str(L[fruit_index][1])
                    new_quantity = get_integer("There are currently {} {}. What would you like to update the quantity of {} to? ".format(original_quantity, fruit_to_update, fruit_to_update))
                    L[fruit_index][1] = new_quantity
                    output = "The quantity of {} has been updated from {} to {}. Select 'Review Fruit' on menu to see changes.".format(fruit_to_update, original_quantity, new_quantity)
                    print(output)
                    print("." * 120)
                    going = False
                    running = False
                else:
                    print("Invalid Input. Please try again.")
        else:
            print("There are no {} in the fruitbowl. Please try again.".format(fruit_to_update))


def main():

    fruit_list = [
        ["Apples", 5],
        ["Bananas", 6],
        ["Peaches", 3],
        ["Strawberries", 15],
        ["Mangoes", 4],
        ["Pears", 1]
    ]

    menu_options = """
    A: Review Fruit
    B: Find Quantity of a Fruit
    C: Add a New Type of Fruit
    D: Record Fruit Consumption
    E: Update Fruit Name or Quantity
    X: Quit
    """

    running = True

    while running == True:
        print(menu_options)

        user_choice = get_string("Enter the corresponding letter for your desired operation: ")

        print("."*120)

        if user_choice == "A":
            review_fruit(fruit_list)
        elif user_choice == "B":
            find_fruit(fruit_list)
        elif user_choice == "C":
            add_new_fruit_type(fruit_list)
        elif user_choice == "D":
            remove_fruit(fruit_list)
        elif user_choice == "E":
            update_fruit(fruit_list)
        elif user_choice == "X":
            print("Thank you for your time!")
            running = False
        else:
            print("Invalid input. Please try again.")
            print("." * 120)

if __name__ == "__main__":
    main()
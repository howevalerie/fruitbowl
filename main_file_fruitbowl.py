def get_string(message):
    my_string = str(input(message)).capitalize()
    return my_string


def get_integer(message):
    my_integer = int(input(message))
    return my_integer


def review_fruit(L):
    for i in range (0, len(L)):
        output = "{:20}: {:<4}".format(L[i][0], L[i][1])
        print(output)
    print("."*80)

def find_fruit(L):
    fruit_to_find = get_string("What fruit would you like to find? ").capitalize()
    if any(fruit_to_find in nested_list for nested_list in L):
        existing_output = "There are {} in the fruitbowl".format(fruit_to_find)
        print(existing_output)
        print("."*80)
    else:
        nonexisting_output = "There are no {} in the fruitbowl".format(fruit_to_find)
        print(nonexisting_output)
        print("."*80)

def add_new_fruit_type(L):
    new_fruit_type = get_string("Enter new fruit type: ")
    new_fruit_quantity = get_integer("Enter quantity of new fruit type: ")
    new_list_item = [new_fruit_type, new_fruit_quantity]
    L.append(new_list_item)
    print("." * 80)
    output = "{} {} have been added to the fruitbowl".format(new_fruit_quantity, new_fruit_type)
    print(output)
    print("."*80)

def remove_fruit(L):
    fruit_to_remove = get_string("What type of fruit was consumed? ")
    if any(fruit_to_remove in nested_list for nested_list in L):
        number_fruit_removed = get_integer("How many {} were consumed? ".format(fruit_to_remove))
        first_index = get_index(L, fruit_to_remove)
        original_quantity = L[first_index][1]
        new_quantity = original_quantity - number_fruit_removed
        L[first_index][1] = new_quantity
        existing_output = "The {} {} have been removed from the fruitbowl".format(number_fruit_removed, fruit_to_remove)
        print(existing_output)
        print("."*80)
    else:
        nonexisting_output = "There are no {} in the fruitbowl and so they cannot be removed".format(fruit_to_remove)
        print(nonexisting_output)
        print("."*80)


def get_index(L, item):
    i = 0
    for x in L:
        if item in x:
            return i
        i +=1

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
    B: Find a Fruit
    C: Add a New Type of Fruit
    D: Record Fruit Consumption
    X: Quit
    """

    running = True

    while running == True:
        print(menu_options)

        user_choice = get_string("Enter the corresponding letter for your desired operation: ")

        print("."*80)

        if user_choice == "A":
            review_fruit(fruit_list)
        elif user_choice == "B":
            find_fruit(fruit_list)
        elif user_choice == "C":
            add_new_fruit_type(fruit_list)
        elif user_choice == "D":
            remove_fruit(fruit_list)
        elif user_choice == "X":
            print("Thank you for your time!")
            running = False
        else:
            print("Invalid Input")
            print("." * 80)

if __name__ == "__main__":
    main()
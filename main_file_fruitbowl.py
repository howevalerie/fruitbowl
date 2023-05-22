def get_string(message):
    my_string = str(input(message)).capitalize()
    return my_string


def get_integer():
    my_integer = int(input(message))
    return my_integer


def review_fruit(L):
    for i in range (0, len(L)):
        output = "{:20}: {:<4}".format(L[i][0], L[i][1])
        print(output)
    print("."*80)

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
    X: List
    """

    running = True

    while running == True:
        print(menu_options)

        user_choice = get_string("Enter the corresponding letter for your desired operation: ")

        print("."*80)

        if user_choice == "A":
            review_fruit(fruit_list)
        elif user_choice == "X":
            print("Thank you for your time!")
            running = False
        else:
            print("Invalid Input")
            running = False

if __name__ == "__main__":
    main()
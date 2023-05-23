def get_index(L, item):
    i = 0
    for x in L:
        if item in x:
            n = i
            print(n)
        i +=1

fruit_list = [
    ["Apples", 5],
    ["Bananas", 6],
    ["Peaches", 3],
    ["Strawberries", 15],
    ["Mangoes", 4],
    ["Pears", 1]
]

get_index(fruit_list, "Mangoes")
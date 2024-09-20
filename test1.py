from random import choice

a_list = ['bobby', 'hadz', 'com', 'a', 'b', 'c']

def main():

    random_element = choice(a_list)
    
    return random_element

    

def main_2():

    i = main()

    print(i)

    a_list.remove(i)
    print(a_list)


main_2()
""" Quick Documentation:
- This py file inlucdes functionality of inputting items, prices, and people.
- We crunch the numbers and divide the total between people. 
"""

from operator import truediv
import sys
import keyboard

def namesInput():
    name_input = input("Enter a name: ")
    # while True:
        # name_input = input("Enter a name: ")
    #     if keyboard.is_pressed('q'):  # if key 'q' is pressed 
    #             print('You Pressed A Key!')
    #             break  # finishing the loop

    

def itemsInput(): #names parameter
    names_list = ["Steven", "Joanne", "Jay", "Xuejin", "Sharon"]

    itemList = {} #items dictionary with (key, value) as (name, price)

    while True:
        item_name = input("What is the item? | Type 'DONE' to proceed: ")
        if item_name == "DONE":
            break
        else:
            item_price = input(f"What is {item_name} price? ")
            itemList[item_name] = item_price
        
    return itemList

def splitCheck():

    print("\033[96m" + "Welcome to Xplitter" + "\033[0m")
    
    title = input("Enter file title:")
    print(title)
    
    # namesInput()
    items_dict = itemsInput()
    print(items_dict)

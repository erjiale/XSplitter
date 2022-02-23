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

    

def itemsInput():
    itemList = []

    while True:
        item_name = input("What is the item? | Type 'DONE' to proceed: ")
        if item_name == "DONE":
            break
        else:
            item_price = input(f"What is {item_name} price? ")
            itemList.append(f"{item_name} ${item_price}")
        
    print(itemList)    


def splitCheck():

    print("\033[96m" + "Welcome to Xplitter" + "\033[0m")
    
    title = input("Enter file title:")
    print(title)
    
    # namesInput()
    itemsInput()
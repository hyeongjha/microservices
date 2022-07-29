from fx_api_client import FxRateApiClient
import json
import os

global fx_rate

fx_rate = None

fx_api_client = FxRateApiClient()

def display_rate():
    print("Currency Rates: ")
    display_search_result(fx_api_client.get_fx_rate().get("currencies"))

def add_rate():
    print("Add New Rate")
    baseCurr = input("Base Currency: ")
    foreign = input("Foreign Currency: ")
    rate = float(input("FX Rate: "))
    newEntry = {
        "baseCurr": baseCurr,
        "foreign": foreign,
        "rate" : rate
    }
    fx_api_client.add_new_fx_rate(newEntry)
    

def display_search_result(result):
    index = 1
    for entry in result:
        print("{}| {}\t| {}\t| {}".format(
            index,
            entry.get("baseCurr"),
            entry.get("foreign"),
            str(entry.get("rate")).rjust(7)))
        index=index+1
    

def clear_screen():
    os.system("cls")
    
def display_menu():
    clear_screen()
    print("Forex App")
    print("\t1. Display Fx Rates")
    print("\t2. Add New Fx Rate")
    print("\t3. Update Fx Rate")
    print("\t4. Delete Fx Rate")
    
    selection = input("\nEnter Selection : ")
    
    clear_screen()
    if selection == "1":
        display_rate()
    elif selection == "2":
        pass
        add_rate()
    elif selection == "3":
        pass
        # update_rate()
    elif selection == "4":
        pass
        # delete_rate()
        
# display_rate()
# add_rate()

display_menu()
#This page is going to work like the following:
#When a user hits create a plan this will create a well organized list that loads the Exercises
import json

class LinkList:
    def __init__(self, name:str, days:int):
        self.name = name
        self.days = days


def main(): #main method that loads and creates workouts
    
    exercise_list = loadX() #loads all exercises form json to list
    
    #interaction_list = loadInt() #loads all interactions from json to list


def loadX():
    
    filename = "plan_3DHKO8" #pulls the file name from frontend to find in the plans folder
    filepath = f"Plans/{filename}/rest_info.json"
    
    with open(filepath, "r") as file:
        data = json.load(file)

    list = [muscles for muscles in data]
    print(list)
    print("I am alive")

#def loadInt():


if __name__ == "__main__":
    main()
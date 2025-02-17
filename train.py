from datetime import *
import random
import os
import json

class Plan():
    """Every Plan will have a unique id. Creating a new Plan will copy the master rest.cfg to the Plan file.
    """
    def __init__(self,plan_id=None):
        if plan_id == None:
            self.rest_info = {}
            with open('C:/Users/elija/OneDrive/Desktop/TrainingApp/rest.cfg','r') as f:
                for line in f:
                    elements = line.strip("\n").split(" ")
                    self.rest_info[elements[0]] = {}
                    try:
                        self.rest_info[elements[0]]["Is Trained"] = True
                        self.rest_info[elements[0]]["Current rest period"] = elements[1]
                        self.rest_info[elements[0]]["Days till ready"] = elements[2]
                    except:
                        self.rest_info[elements[0]]["Is Trained"] = False

                print(self.rest_info)

            while True:
                plan_id="plan_"
                for i in range(0,6,1):
                    plan_id = plan_id + '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[random.randint(0,35)]

                if not os.path.exists('C:/Users/elija/OneDrive/Desktop/TrainingApp/'+plan_id):
                    break

            self.id=plan_id.upper()
            os.mkdir('C:/Users/elija/OneDrive/Desktop/TrainingApp/Plans/'+plan_id)
            with open('C:/Users/elija/OneDrive/Desktop/TrainingApp/Plans/'+plan_id+'/rest_info.json', 'w') as f:
                json.dump(self.rest_info, f, indent = 4)

        else:
            self.id=plan_id

        print(self.id)

test = Plan()

#can edit rest.cfg
#create json file under unique plan id

#cannnot generate plan
#create unique calendar
#log existing workouts
#auto recommend workouts

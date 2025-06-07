from django.db import models

class Ski_Area(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length = 255)

    def __str__(self):
        return f"{self.name} in {self.location}"
                
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)       
    
    epic_PassNumber = models.BigIntegerField(null=True, verbose_name='Passnumber list on the Epic Mix app.')
    physical_PassNumber = models.BigIntegerField(null=True, verbose_name='Passnumber listed on your printed Epic pass.')
            
    class Meta:
        permissions = [
            ('create_exchange', 'Can exhange available schedule'),
            ('delete_exchange', 'Can remove exchanged schedule'),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

import os
import json

def load_file():
    json_file = "resorts.json"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, json_file)

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON in file: {json_file}")
    except Exception as e:
        print(f"An error occurred with file {json_file}: {e}")


def load_resorts():
    resort_list = load_file()
    
    for resort in resort_list["vail"]:
        #print( f"name = {resort["name"]}, location = {resort["location"]}")
        new_resort = Ski_Area( name = resort["name"] , location = resort["location"] )
        try:
            new_resort.save()
        except Exception as e:
            print(e)

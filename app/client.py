import requests
import yaml

def create_person(filename: str):
    files = {"file": open(filename, "rb")}
    response = requests.post("http://localhost:8000/person", files=files)
    print(response.text)    
    if response.status_code == 200:
        print("Person created successfully!")
    else:
        print("Error creating person.")
create_person(filename="person.yaml")
def get_person(id: str):
    response = requests.get(f"http://localhost:8000/person/{id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error retrieving person.")
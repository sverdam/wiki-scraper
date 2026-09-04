
import random as rand
import json

# def getDummyAnswer(data:dict, key):
#     for character in data.keys():
#         if key in data[character]:
#             print(f'{character}[{key}]')
#             print(data[character][key])

def randomData(data:dict, key: str, multiple) -> str:

    characters = list(data.keys())
    character = data[characters[rand.randrange(0, len(characters))]]

    if key not in character:
        return ""

    if multiple:
        attributes = character[key]
        return attributes[rand.randrange(0, len(attributes))]
    
    return character[key]

def separate(text:str):
    print(f"RAW TEXT <{text}>")
    text = str(text)
    if "(" not in text:
        return text, "" 

    if len(text) < 3:
        return "", ""    

    x, y = text.split(" (", 1)
    y = y.rstrip(")")

    return x, y

def generateRelationshipQuestion(data:dict, character:str):
    relationships = data[character]["Relationships"]
    randomRelationShip = relationships[rand.randrange(0, len(relationships))]
    rel = separate(randomRelationShip)

    if (rel[1] == ""):
        print("BAD RELATIONSHIP")
        return {}

    if "\u00e9" in rel[1]:
        print("BAD RELATIONSHIP")
        return {}

    print("RELATIONSHIP: ", rel)
    options = [f"{rel[1]}"]

    while len(options) < 4:
        new_option = randomData(data, "Relationships", True)
        new_option = separate(new_option)[1]

        if new_option == "" or new_option == "u00e9":
            continue

        if new_option in options:
            continue
        options.append(new_option)

    
    newQuestion = {
        "question": f"What is {rel[0]}'{'s' if rel[0][-1] != 's' else ''} relationship to {character}?",
        "answer": f"{rel[1]}",
        "options": options
    }


    return newQuestion


def generateAKA(data:dict, character:str):
    relationships = data[character]["Also known as"]
    randomRelationShip = relationships[rand.randrange(0, len(relationships))]
    rel = separate(randomRelationShip)

    if (rel[1] == ""):
        print("BAD Also known as")
        return {}

    if "\u00e9" in rel[1]:
        print("BAD Also known as")
        return {}

    print("AKA: ", rel)
    options = [f"{rel[1]}"]

    while len(options) < 4:
        new_option = randomData(data, "Also known as", True)
        new_option = separate(new_option)[1]

        if new_option == "" or new_option == "u00e9":
            continue

        if new_option in options:
            continue
        options.append(new_option)

    newQuestion = {
        "question": f"Who calls {character} '{rel[0]}'?",
        "answer": f"{rel[1]}",
        "options": options
    }


    return newQuestion


def generateLocationQuestion(data:dict, character:str):
    places = data[character]["Appearances"]
    place = places[rand.randrange(0, len(places))]

    
    options = [f"{place}"]

    
    while len(options) < 4:
        new_option = randomData(data, "Appearances", True)

        if new_option == "" or new_option == "u00e9":
            continue

        if new_option in options:
            continue

        if new_option in places:
            continue

        options.append(new_option)

    newQuestion = {
        "question": f"Where does {character} appears?",
        "answer": f"{place}",
        "options": options
    }

    return newQuestion

def generateQuestion(data:dict, character:str, field:str):
    if field == "Relationships":
        return generateRelationshipQuestion(data, character)

    if field == "Also known as":
        return generateAKA(data, character)

    if field == "Appearances":
        return generateLocationQuestion(data, character)
        
    return {}


def generate(data:dict):
    questions = []
    multiplier = 4
    for i in range(4):
        for character in data.keys():
            for field in data[character].keys():
                newQuestion = generateQuestion(data, character, field)
                if not newQuestion:
                    continue

                questions.append(newQuestion)


    saveData(questions)

    return questions


def saveData(data):
    jsonString = json.dumps(data, indent=4, sort_keys=True)
    print(jsonString)

    with open("questions.json", "w") as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)

# RELATIONSHIP
# quien es el hermano de este personaje?
# X es el que cosa de este personaje?

# ALSO KNOWN AS
# 

# PRONOUNS



#   question: "lol?",
#         options: [
#             "A",
#             "B",
#             "C",
#             "D"
#         ],
#         answer: "D"
#https://www.dataquest.io/blog/python-api-tutorial/

#Dota 2 API Project

import requests
import json
from dota2_heroes_class import heroes_list

baseurl = "https://api.opendota.com/api/"
response = requests.get(baseurl)

#possible player IDs to test
#-----------------------------

#113331514 - Miposhka
#87278757  - Puppey
#101695162 - fy
#86745912  - Arteezy

#json test helper function
#--------------------------------------------------------------------------

def jdumps(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#dota2 helper functions
#--------------------------------------------------------------------------

#tester function to see inside player profile
def get_player_profile_info(id):
    players_rep = requests.get(baseurl + "players/{}".format(id))
    return players_rep.json()

def get_player_name(id):
    players_rep = requests.get(baseurl + "players/{}".format(id))
    return players_rep.json()["profile"]["personaname"]


def hero_id_converted(hero_id):
    for hero in heroes_list["result"]["heroes"]:
        if int(hero_id) == int(hero["id"]):
            return hero["name"].replace("npc_dota_hero_", "").replace("_", " ").title()

def get_heroes_data(id):
    heroes_played_list = []
    players_rep = requests.get(baseurl + "players/{}/heroes".format(id))
    for val in players_rep.json():
        heroes_played_list.append((hero_id_converted(val["hero_id"]), val["games"]))
    heroes_played = sorted(heroes_played_list, key = lambda item: item[1])
    return heroes_played

#actual dota 2 functions
#------------------------------------------------------

def get_least_heroes_played(id, heroes_num):
    heroes_list_sorted = get_heroes_data(id)
    top_heroes_list = []
    for i, hero in enumerate(heroes_list_sorted):
        if i < heroes_num:
            top_heroes_list.append(hero[0])
        else:
            break
    return ", ".join(top_heroes_list)

def get_top_heroes_played(id, heroes_num):
    heroes_list_sorted = get_heroes_data(id)
    top_heroes_list = []
    for i, hero in enumerate(reversed(heroes_list_sorted)):
        if i < heroes_num:
            top_heroes_list.append(hero[0])
        else:
            break
    return ", ".join(top_heroes_list)

#execute code:
#--------------------------------------------------------------------------

def input_project():
    id = input("Enter steam32 ID")
    try:
        data_search = input(

            """The username is {}. Type in the corresponding number to get data for:
            1. Top Played Heroes
            2. Least Played Heroes
            3. uhohstinky
            4. idunnokekw""".format(get_player_name(id)))

        if data_search == "1":
            heroes_num = input("Up to how many heroes? Type a number.")
            print("{}'s most played heroes are: {}.".format(get_player_name(id), get_top_heroes_played(id, int(heroes_num))))

            yes_or_no = input("Would you like to do anything else? Type 'Y' to continue, type anything else to end")
            if yes_or_no.upper() == "Y":
                input_project()
            else:
                print("End")

        if data_search == "2":
            heroes_num = input("Up to how many heroes? Type a number.")
            print("{}'s most least played heroes are: {}.".format(get_player_name(id), get_least_heroes_played(id, int(heroes_num))))

            yes_or_no = input("Would you like to do anything else? Type 'Y' to continue, type anything else to end")
            if yes_or_no.upper() == "Y":
                input_project()
            else:
                print("End")
        else:
            print("Not yet implemented or out of bounds - End")
    except:
        print("Not valid ID - End")

input_project()

#past iterations of dota2 functions
#--------------------------------------------------------------------------

#def get_top_hero(id):
#    players_rep = requests.get(baseurl + "players/{}/heroes".format(id))
#    heroes_win = 0
#    hero_id = 0
#    for val in players_rep.json():
#        if val["games"] > heroes_win:
#            hero_id = val["hero_id"]
#            heroes_win = val["games"]
#    return hero_id_converted(hero_id)

#def get_least_hero(id):
#    players_rep = requests.get(baseurl + "players/{}/heroes".format(id))
#    heroes_win = 100000
#    hero_id = 0
#    for val in players_rep.json():
#        if val["games"] < heroes_win:
#            hero_id = val["hero_id"]
#            heroes_win = val["games"]
#    return hero_id_converted(hero_id)

#-------------------------------------------------------------------------------
#testing grounds

#print(get_player_name(87278757))
#print(get_top_heroes_played(87278757, 5))
#print(get_least_hero(87278757))
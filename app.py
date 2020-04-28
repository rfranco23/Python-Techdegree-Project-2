import constants
import copy
import random


teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

experienced = []
inexperienced = []

panthers = []
bandits = []
warriors = []

panthers_guardians = []
bandits_guardians = []
warriors_guardians = []

player_guardians = [panthers_guardians, bandits_guardians, warriors_guardians]

panthers_height = []
bandits_height = []
warriors_height = []

player_height = [panthers_height, bandits_height, warriors_height]

panthers_names = []
bandits_names = []
warriors_names = []

player_names = [panthers_names, bandits_names, warriors_names]


def clean_player_data():
    for player in players:
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split(" and ")
        if player['experience'].lower() == "yes":
            player['experience'] = True
            experienced.append(player)
        else:
            player['experience'] = False
            inexperienced.append(player)
            
            
def balance_teams(team):
    while len(experienced) != 0 and len(team) < 3:
        team.append(experienced.pop(random.randrange(len(experienced))))
        
    while len(inexperienced) != 0 and len(team) < 6:
        team.append(inexperienced.pop(random.randrange(len(inexperienced))))
        
    
def names(name, team):
    for player in team:
        name.append(player['name'])
        
        
def avg_height(height, team):
    for player in team:
        height.append(player['height'])
        
        
def guardians(guardian, team):
    for player in team:
        player['guardians'] = (', ').join(player['guardians'])
        guardian.append(player['guardians'])

        
def main_function():
    clean_player_data()
    balance_teams(panthers)
    balance_teams(bandits)
    balance_teams(warriors)
    names(panthers_names, panthers)
    names(bandits_names, bandits)
    names(warriors_names, warriors)
    avg_height(panthers_height, panthers)
    avg_height(bandits_height, bandits)
    avg_height(warriors_height, warriors)
    guardians(panthers_guardians, panthers)
    guardians(bandits_guardians, bandits)
    guardians(warriors_guardians, warriors)
        

if __name__ == '__main__':
    # Execute code within the "main_function" function.
    main_function()
    app_running = True
    
    while app_running:
        print("\n**** MENU ****\n\nPlease choose from the following:\n1) Display Team Stats\n2) Quit\n\n")
        option = input("Please choose an option: ")
        if option == "1":
            print("\nPick from the following teams:\n--------------------\n\n1) Panthers\n2) Bandits\n3) Warriors\n\n")
            team_number = input("Please choose an option (1, 2 or 3): ")
            try:

                def doc_string():
                    return """
                
Team {} Stats
--------------------

Total Players: {}
Experienced Players: {}
Inexperienced Players: {}
Player Names: {}
Average Player Height: {} inches
Player Guardians: {}
                    
                    """.format(
                        teams[int(team_number) - 1],
                        len(panthers),
                        3, 3,
                        (', ').join(player_names[int(team_number) - 1]),
                        round(sum(player_height[int(team_number) - 1]) / len(player_height[int(team_number) - 1])),
                        (', ').join(player_guardians[int(team_number) - 1]))
            
                print(doc_string())
                input("Press Enter to continue...")
            except (ValueError, IndexError) as err:
                print("{}. Please choose again.".format(err))
                input("Press Enter to continue... ")
                
        elif option == "2":
            app_running = False
        else:
            print("\"{}\" is not a valid entry, please choose an available option. ".format(option))
            input("Press Enter to continue... ")
    
import csv  # Importing csv module

if __name__ == "__main__":

    player_list = []  # assigning the player list to an empty list

    with open('soccer_players.csv', 'r') as file:  # Opening the csv file
        soccer_players = csv.reader(file, delimiter=',')
        rows = list(soccer_players)  # Assigning the csv file to player_list list
        for row in rows:
            player_list += rows

    # Assigning the player_list to the teams evenly according to their experience.
    dragons = []
    dragons += player_list[0:4]
    dragons += player_list[4:7]

    sharks = []
    sharks += player_list[0]
    sharks += player_list[8:10]
    sharks += player_list[13]
    sharks += player_list[10:13]

    raptors = []
    raptors += player_list[0]
    raptors += player_list[16:19]
    raptors += player_list[7]
    raptors += player_list[14:16]

    # Converting the list in to string so that it can be added to a text file.

    dragon_roster = ''
    for players in dragons:
        for i in range(len(players)):
            dragon_roster += players[i]
            dragon_roster += ', '

        dragon_roster += '\n'

    # Adding the text to a file named teams.txt
    with open("teams.txt", "a") as file:
        file.write('Dragon \n')
        file.write(dragon_roster)
        file.write('\n')

    # Converting the list in to string so that it can be added to a text file.
    sharks_roster = ''
    for players in sharks:
        for i in range(len(players)):
            sharks_roster += players[i]
            sharks_roster += ', '

        sharks_roster += '\n'

    # Adding the text to a file named teams.txt
    with open("teams.txt", "a") as file:
        file.write('Sharks \n')
        file.write(sharks_roster)
        file.write('\n')

    # Converting the list in to string so that it can be added to a text file.
    raptors_roster = ''
    for players in raptors:
        for i in range(len(players)):
            raptors_roster += players[i]
            raptors_roster += ', '

        raptors_roster += '\n'

    # Adding the text to a file named teams.txt
    with open("teams.txt", "a") as file:
        file.write('Raptors \n')
        file.write(raptors_roster)
        file.write('\n')

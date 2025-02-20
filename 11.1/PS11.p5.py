
from ast import Name


def load_players(file_path):
    player_names = []
    batting_averages = []
    with open("C:\CIS106\Section 11\players.txt", 'r') as file:
        for line in file:
            name, average = line.strip().split(',')
            player_names.append(name)
            batting_averages.append(float(average))
    return player_names, batting_averages

def display_players(player_names, batting_averages):
    print("Player Names and Batting Averages:")
    for name, average in zip(player_names, batting_averages):
        print(f"{name}: {average:.3f}")

def search_player(player_names, batting_averages, last_name):
    for name, average in zip(player_names, batting_averages):
        if name.lower() == last_name.lower():
            return name, average
    return None, None

def main():
    player_names, batting_averages = load_players('players.txt')
    display_players(player_names, batting_averages)
    
    while True:
        last_name = input("Enter a player's last name to search (or 'exit' to quit): ")
        if last_name.lower() == 'exit':
            break
        name, average = search_player(player_names, batting_averages, last_name)
        if name:
           print(f"Found: {name} with a batting average of {average:.3f}")
        else:
           print("Player not found.")
  
if __name__ == "__main__":
    main()


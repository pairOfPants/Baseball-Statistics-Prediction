import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://umbcretrievers.com/sports/baseball/stats")
soup = BeautifulSoup(response.text, 'html.parser')
        
# Extract information from the page
player_rows = soup.find_all('tr',class_='stat_doesnt_meet_min')
player_rows2 = soup.find_all('tr',class_='stat_meets_min')
dictionary = {}
stat_type = ['AVG',"OPS","GP-GS",'AB','R','H',"2B",'3B','HR','RBI','TB',"SLG%",'BB','HBP','SO',"GDP",'OB%','SF','SH','SB']


def pull_stats(player_rows,dictionary,stat_type):
    for player_row in player_rows:
        # Extract data from each row
        player_name = player_row.find('a', class_='hide-on-medium-down').get_text(strip=True)
        if player_name not in dictionary:
            dictionary[player_name] = {}
        for stat in stat_type:
            if player_row.find('td', {'data-label': stat}) != None:
                player_stat = player_row.find('td', {'data-label': stat}).get_text(strip=True)
                if stat not in dictionary[player_name]:
                    dictionary[player_name][stat] = player_stat


pull_stats(player_rows,dictionary,stat_type)
pull_stats(player_rows2,dictionary,stat_type)


# Convert dictionary to a JSON string
json_data = json.dumps(dictionary, indent=2)  

# Specify the file path where you want to save the data
file_path = 'stats.txt'

# Write the JSON string to the file
with open(file_path, 'w') as file:
    file.write(json_data)

print(f"Stats have been saved to {file_path}")
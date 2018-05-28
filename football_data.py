import requests
from time import sleep
import random


def call_football(url):
    token = {'X-Auth-Token': '7eecbfb6d62b4e5dbd91a81d316b8cc3'}
    return requests.get(url, headers = token).json()


url = 'http://api.football-data.org/v1/competitions/459/leagueTable'
standings = call_football(url)
football_data = []
for standing in standings['standing']:
    team_data = call_football(standing['_links']['team']['href'])
    squad_market_value = team_data['squadMarketValue'] if team_data['squadMarketValue']\
        else random.randint(10000000, 100000000)
    football_data.append({'squadMarketValue': squad_market_value, 'losses': standing['losses']})
    sleep(0.1)

print(football_data)
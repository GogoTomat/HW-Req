import requests
import pprint

API = 'https://superheroapi.com/api/2619421814940190'

HEROES_NAMES = {'Hulk', 'Captain America', 'Thanos'}


heroes = {}
for hero in HEROES_NAMES:
    r = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')
    id = r.json()["results"][0]["id"]
    heroes[str(id)] = {'name': hero, "iq": 0}

for id in heroes:
    r = requests.get(f'https://superheroapi.com/api/2619421814940190/{id}/powerstats/')
    intel = r.json()["intelligence"]
    heroes[id]['iq'] = intel

maxIq = 0
smartestHero = 'none'
for id in heroes:
    if int(heroes[id]['iq']) > maxIq:
        maxIq = int(heroes[id]['iq'])
        smartestHero = heroes[id]['name']

print(smartestHero)

from __future__ import print_function
import requests
import json

mtgResponse = requests.get(
    'https://api.magicthegathering.io/v1/cards?gameFormat=Modern&text=opponent,damage,discards',
    headers={"Accept": "application/json"})

cardCollection = json.loads(mtgResponse.text)

for card in cardCollection['cards']:
    print("card name: {}, mana cost: {}, type: {}"
          .format(card['name'], card['manaCost'], card['type']))


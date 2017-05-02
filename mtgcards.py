from __future__ import print_function
import requests
import json

mtgResponse = requests.get(
    'https://api.magicthegathering.io/v1/cards?gameFormat=Modern&text=opponent,damage,discards',
    headers={"Accept": "application/json"})

cards = json.loads(bytes(bytearray(mtgResponse.text, encoding='utf-8')))

for card in cards:
    print("card name: {}, mana cost: {}, type: {}, text: {}"
          .format(card.name, card.manaCost, card.type, card.text))


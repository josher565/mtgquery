from __future__ import print_function
import requests
import json
import codecs
import sys

mtgResponse = requests.get(
    'https://api.magicthegathering.io/v1/cards?gameFormat=Modern&color=B,R,U&text=opponent,damage,draw',
    headers={"Accept": "application/json"})

cardCollection = json.loads(mtgResponse.text)


UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

for card in cardCollection['cards']:
    print(u"\n\ncard name: {}, mana cost: {}, type: {}, rarity: {} \ntext: {}"
          .format(card['name'], card['manaCost'], card['type'], card['rarity'], card['text']))

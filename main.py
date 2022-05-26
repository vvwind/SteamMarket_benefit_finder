import json
import csv
import requests
from bs4 import BeautifulSoup


steam_link = 'https://steamcommunity.com/market/listings/570/'
ur_cookies = 'your cookies'

def price_finder(one_item):
    default_value = 0.0
    try:
        newurl = steam_link + one_item
        response = requests.get(newurl, headers=headers)
        soup_price = BeautifulSoup(response.text, 'lxml')
        quotes = soup_price.find_all('span', {'class': 'market_listing_price market_listing_price_with_fee'})
        price_list_str = list(map(lambda x : x.text.strip()[:-5], quotes))
        price_list_floated = list(map(lambda x: float(x.replace(",", ".")), price_list_str))
        price_list_floated.sort()
        print(price_list_floated)
        return price_list_floated[0]
    except:
        return default_value


with open("stonks.csv", "w") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(("Set_Name", "STONKS"))



heroes = ['abaddon', 'alchemist', 'ancient-apparition', 'anti-mage', 'arc-warden', 'axe', 'bane', 'batrider',
          'beastmaster', 'bloodseeker', 'bounty-hunter',
          'brewmaster', 'bristleback', 'broodmother', 'centaur-warrunner',
          'chaos-knight', 'clinkz', 'clockwerk', 'crystal-maiden', 'dark-seer', 'dark-willow', 'dazzle',
          'death-prophet', 'disruptor', 'doom', 'dragon-knight',
          'drow-ranger', 'earth-spirit', 'earthshaker', 'elder-titan', 'ember-spirit', 'enchantress', 'enigma',
          'grimstroke', 'gyrocopter', 'huskar', 'invoker', 'jakiro', 'juggernaut', 'keeper-of-the-light', 'kunkka',
          'legion-commander', 'leshrac', 'lich',
          'lifestealer', 'lina', 'lion', 'lone-druid', 'luna',
          'lycan', 'magnus', 'medusa', 'meepo', 'mirana', 'monkey-king', 'morphling', 'naga-siren', 'natures-prophet',
          'necrophos', 'night-stalker', 'nyx-assassin',
          'ogre-magi', 'omniknight',
          'oracle', 'outworld-devourer', 'pangolier', 'phantom-assassin', 'phantom-lancer', 'phoenix', 'puck', 'pudge',
          'pugna', 'queen-of-pain', 'razor', 'riki', 'rubick',
          'sand-king', 'shadow-demon', 'shadow-fiend',
          'shadow-shaman', 'silencer', 'skywrath-mage', 'slardar', 'slark', 'sniper', 'spectre', 'spirit-breaker',
          'storm-spirit', 'sven', 'techies',
          'templar-assassin', 'terrorblade', 'tidehunter', 'timbersaw', 'tinker', 'tiny', 'treant-protector',
          'troll-warlord', 'tusk', 'underlord',
          'undying', 'ursa', 'vengeful-spirit', 'venomancer', 'viper', 'visage', 'warlock', 'weaver', 'windranger',
          'winter-wyvern', 'witch-doctor', 'wraith-king', 'zeus', 'faceless-void']

headers = {'Cookie': ur_cookies
           , 'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
           , 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
           }

with open('all_heroes_sets.json') as d:
    dictData = json.load(d)
for it in heroes:
    for k, v in dictData[f"{it}"].items():
        print(f" Checking hero: {it}  Bundle: {k}")
        s = 0
        head_value = price_finder(k)
        if head_value < 1:
            continue
        for i in v:
            value = price_finder(i)
            s += value

        s -= s * 0.13
        s -= head_value

        if s < 1:
            continue
        else:
            newstonks = [k, s]
            with open("stonks.csv", "a") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(newstonks)


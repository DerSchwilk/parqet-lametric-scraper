import json
import requests
import os


def get_json():
    with open('template.json', "r") as template_file:
        template_json = json.load(template_file)
        json_data = scrape()
        net_value = get_net_value(json_data)

        template_json['frames'][1]['text'] = str(int(get_valuation(json_data))) + "€"
        template_json['frames'][3]['icon'] = get_net_value_icon(net_value)
        template_json['frames'][3]['text'] = str(net_value) + "%"
        return template_json


def get_valuation(json_value):
    return json_value['performance']['value']


def get_net_value(json_value):
    return json_value['performance']['returnNet']


def get_net_value_icon(net_value):
    if net_value >= 0:
        # Green up arrow
        return 120
    else:
        # Red down arrow
        return 124


def scrape():
    url = "https://api.parqet.com/v1/portfolios/" + os.environ['PARQET_PORTFOLIO_ID']
    print("Getting information from: " + url)
    parsed_url = requests.get(url)
    text = parsed_url.text
    return json.loads(text)


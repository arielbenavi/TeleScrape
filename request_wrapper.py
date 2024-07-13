import time
import random
import requests


def get_random_user_agent():
    """
    :recieves: None
    :return: Random user agent string.
    """
    # TODO: change dir
    user_agents = '/Users/arismac/Sync/win_mac_sync/dev/networker/user_agents.txt'
    with open(user_agents, encoding='utf8') as f:
      user_agents_list = [_.strip() for _ in f.readlines()]
    
    headers = {
      "User-Agent": random.choice(user_agents_list)
    }

    return headers


def af_request(url, headers=None, cookies=None):
    """
    :recieves: None
    :return: Request object with random user agent.
    """
    time.sleep(0.5)
    if not headers: headers = get_random_user_agent()
    return requests.get(url, headers=headers, cookies=cookies)


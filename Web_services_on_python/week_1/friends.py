import requests
from operator import itemgetter

ACCESS_TOKEN = 'TOKEN'

def calc_age(uid):
    r = requests.get('https://api.vk.com/method/users.get?v=5.71&access_token={1}&user_ids={0}'
                     .format(uid, ACCESS_TOKEN))
    id  = r.json()['response'][0]['id']
    friends = requests.get('https://api.vk.com/method/friends.get?v=5.71&access_token={1}'
                           '&user_id={0}&fields=bdate'.format(id, ACCESS_TOKEN))
    dates = friends.json()['response']['items']
    clear_dates = dict()
    for i in dates:
        if 'bdate' in i:
            date = i['bdate']
            # print(date)
            if len(date) > 5:
                year = 2020 - int(date[-4:])
                if year not in clear_dates:
                    clear_dates[year] = 0
                clear_dates[year] += 1
    final = list()
    for key, value in clear_dates.items():
        final.append((key, value))
    final.sort(key=itemgetter(0))
    final.sort(key=itemgetter(1), reverse=True)
    return final

if __name__ == '__main__':
    res = calc_age('lyokhatsar')
    print(res)



import requests
from datetime import datetime

ACCESS_TOKEN = "17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711"
VERSION = "5.81"
USER_URL = "https://api.vk.com/method/users.get"
FREINED_URL = "https://api.vk.com/method/friends.get"


def get_user_id(uid):
    res = requests.get(
        USER_URL, params={"v": VERSION, "access_token": ACCESS_TOKEN, "user_ids": uid}
    )
    json_res = res.json()
    try:
        return json_res["response"][0]["id"]
    except:
        pass


def get_user_friends(uid):
    res = requests.get(
        FREINED_URL,
        params={
            "v": VERSION,
            "access_token": ACCESS_TOKEN,
            "user_id": uid,
            "fields": "bdate",
        },
    )
    res_json = res.json()
    try:
        return res_json["response"]["items"]
    except:
        pass


def calc_age(uid):
    id = get_user_id(uid)
    if not id:
        return
    friends = get_user_friends(id)

    if not friends:
        return

    friends_dic = {}
    for friend in friends:
        if 'bdate' not in friend:
            continue
        bdate = friend['bdate']
        bdate = bdate.split('.')
        if len(bdate) < 3:
            continue
        diff = int(datetime.now().year) - int(bdate[2])
        friends_dic[diff] = friends_dic.get(diff, 0)  + 1
    return sorted(friends_dic.items(), key=lambda v: (-v[1], v[0]))
    



if __name__ == "__main__":
    res = calc_age("reigning")
    print(res)

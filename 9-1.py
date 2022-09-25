import requests
heroes_list = ["Hulk", "Captain America", "Thanos"]

## Способ первый. Наверное, методологически верный, но очень долгий
# heroes_rating = {}
# for id in range(1,732):
#     url = f"https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/{id}.json"
#     if requests.get(url).status_code != 404:
#         if requests.get(url).json().get("name") in heroes_list:
#             heroes_rating[requests.get(url).json().get("name")] = requests.get(url).json().get("powerstats").get("intelligence")
# for k,v in heroes_rating.items():
#     if v > int:
#         int = v
# for k, v in heroes_rating.items():
#     if v == int:
#         print(k)

## Способ второй
heroes_rating = {}
int = 0
url = f"https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
json = requests.get(url).json()
for id in range(0, len(json)):
    if json[id].get("name") in heroes_list:
        heroes_rating[json[id].get("name")] = json[id].get("powerstats").get("intelligence")
for k,v in heroes_rating.items():
    if v > int:
        int = v
for k, v in heroes_rating.items():
    if v == int:
        print(k)



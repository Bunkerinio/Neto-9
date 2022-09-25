import requests
import time

to_date = int(time.time())
number_of_days = 2 # выбрать необходимое количество дней
from_date = int(time.time()) - 86400*number_of_days
tag = "Python" # выбрать необходиый тэг

url = f"https://api.stackexchange.com/2.3/questions?fromdate={from_date}&todate={to_date}&order=desc&sort=activity&tagged={tag}&site=stackoverflow"
json = requests.get(url).json()["items"]
print({"Автор темы": "Вопрос"})
for i in range(0, len(json)):
    name = json[i]["owner"]["display_name"]
    title = json[i]["title"]
    print({name : title})

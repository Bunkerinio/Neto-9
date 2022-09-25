import requests
with open("token.txt") as file: # Указать txt с токеном
    token = file.read()
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload_file(self, loadfile, savefile):
        res = requests.get(f'{URL}/upload?path={savefile}', headers=headers).json()
        with open(loadfile, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)


if __name__ == '__main__':
    uploader = YaUploader(token)
    savefile = r"disk:/Загрузки/test txt.txt" # локация на Диске и имя загружаемого файла
    loadfile = r"C:\Users\bunke\PycharmProjects\Neto 9-2\test txt.txt" # местоположение загружаемого файла на ПК
    result = uploader.upload_file(loadfile, savefile)
# path = "disk:/Загрузки/"
# pprint(requests.get(f"{URL}?path={path}", headers=headers).json())
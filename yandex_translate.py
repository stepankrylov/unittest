import requests


def translate(i, lang_1, lang_2='de'):
  
  URL = 'https://translate.yandex.net/api/v1/tr.json/translate'

  tr_headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36',
    }

  tr_params = {
  'id': '881cd233.5d668a7b.e3f869d8-0-0',
  'srv': 'tr-text',
  'lang': f'{lang_1}-{lang_2}',
  'text': f'{i}'
    }
  resp = requests.get(URL, headers=tr_headers, params=tr_params)
  s = resp.status_code
  print(s)
  t = resp.json()['text'][0]
  print(t)
  return t, s
if __name__ == "__main__":
    translate('Привет', 'ru')
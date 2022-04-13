from requests import get, utils
response = get('http://geekbrains.ru')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(content)
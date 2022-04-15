from requests import get, utils


response = get('http://geekbrains.ru')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(encodings)
#print(response.status_code)
#print(type(response))
#print(dir(response))
#print(response.content.decode(encoding=response.encoding))
#print(response.text)
#content = response.text
#for el in content.split('href="')[1:]:
#    print(el.split('"')[0])
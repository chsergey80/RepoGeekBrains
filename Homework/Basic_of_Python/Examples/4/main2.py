from requests import get

response = get('http://geekbrains.ru')
#print(response.status_code)  # 200 ok
# print(response.content.decode(encoding=response.encoding))
content = response.text
for el in content.split('href="')[1:]:
    print(el.split('"')[0])


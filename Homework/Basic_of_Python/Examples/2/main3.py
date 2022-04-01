msg = '!привет,     я обычная строка!!!'
msg_tmp = list(msg)
new_msg = ','.join(msg_tmp)
print(new_msg)
print(msg.upper())  # lower
print(msg.title())
print(msg.capitalize())
a, b, c, d = msg.split()
print(a)
print(msg.rstrip())  #r, l
print(msg.islower())  #isupper, istitle
print(msg.endswith('!'))  # startswith
print(msg.count("я"))
print(msg.upper().capitalize().count("я"))
print(msg.replace("я", 'ЯЯЯ'))
print(msg.index('я'))
print(msg.find("я", 30))





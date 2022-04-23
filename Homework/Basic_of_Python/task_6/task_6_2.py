"""
Задание 6.2.*(вместо 1) Найти IP адрес спамера и кол-во отправленных им запросов по данным файла логов из предыдущего
задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
"""

def parse_log(pth_file):
    if pth_file:
        with open(pth_file, "r", encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield (ip, rsp, pth)


def find_spamer(pth_file):
    if not pth_file:
        return None

    db = {}
    for log in parsed_log:
        if not db.get(log[0]):
            db[log[0]] = {"count": 1, "files": set([log[2]])}
        else:
            db[log[0]]["count"] += 1
            db[log[0]]["files"].add(log[2])

    return max(db.items(), key=lambda x: x[1]["count"])


if __name__ == "__main__":
    parsed_log = parse_log("./nginx_logs.txt")
    spamer = find_spamer(parsed_log)
    print(spamer)

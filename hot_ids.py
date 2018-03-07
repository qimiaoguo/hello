def get_all_hot_ids():
    file = open("hotids.txt")
    hot_ids = set()
    while 1:
        line = file.readline()
        if not line:
            break
        hot_ids.add(int(line.strip('\n')))
    file.close()
    hot_ids
    return hot_ids

all_hot_ids = get_all_hot_ids()

print all_hot_ids

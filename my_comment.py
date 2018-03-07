import random


def get_all_comments():
    file = open("mycomments.txt")
    comments = list()
    while 1:
        line = file.readline()
        if not line:
            break
        comments.append(line.strip('\n'))
    file.close()
    return comments

all_comments = get_all_comments()
length = len(all_comments)


def get_random_comment():
    return all_comments[random.randint(0, length - 1)]

#print get_random_comment()

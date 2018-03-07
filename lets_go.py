# coding=utf8
from time import sleep

from bihu import *
from hot_ids import all_hot_ids
from my_comment import get_random_comment

if __name__ == '__main__':
    art_id = 44601
    try_times = 0
    while 1:
        #x -= 1
        # article = get_unlogin_article(art_id)
        # user_id = article['data']['userId'] if article['res'] == 1 else 0
        # if user_id == 0:
        #     print 'article %d not existed, wait for 7 seconds' %art_id
        #     try_times += 1
        #     if try_times > 2:
        #         art_id += 1
        #         try_times = 0
        #     sleep(7)
        #     continue
        # try_times = 0
        # if user_id in all_hot_ids:
        #     up_vote(art_id)
        #     print 'vote to user %s with article %d' %(user_id, art_id)
        print art_id
        create_comment(art_id, get_random_comment())
        art_id += 1
        sleep(4)

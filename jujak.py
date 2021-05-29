#! /usr/bin/python3
import requests
from time import sleep
SLEEP_INTERVAL = 15

proxy = {
    'http' : 'http://127.0.0.1:5566',
    'https' : 'http://127.0.0.1:5566'
}

g_id = input('gallery_id : ')
g_no = input('board_number : ')

if len(g_id) == 0:
    g_id = 'programming'
if len(g_no) == 0:
    g_no = '1741984'

count = 50
while count:
    sess = requests.Session()
    res = sess.get(f'https://gall.dcinside.com/board/view/?id={g_id}&no={g_no}', headers={'User-Agent' : 'test'})
    if res.status_code == '404':
        print("something goes wrong...")
        exit(1)
    sess.cookies.set(f'{g_id}{g_no}_Firstcheck', 'Y', domain="dcinside.com")
    res = sess.post('https://gall.dcinside.com/board/recommend/vote', data={
        "ci_t" : res.cookies['ci_c'],
        "id" : g_id,
        "no" : g_no,
        "mode": "U" ,# U for up, D for down
        "code_recommend" : "undefined",
        "_GALLTYPE_" : "G", # G M 
        "link_id" : g_id
    }, headers={
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Origin': 'https://gall.dcinside.com',
        'Referer': f'https://gall.dcinside.com/board/view/?id={g_id}&no={g_no}',
    }, proxies=proxy)
    res = sess.post('https://gall.dcinside.com/board/recommend/vote', data={
        "ci_t" : res.cookies['ci_c'],
        "id" : g_id,
        "no" : g_no,
        "mode": "U" ,# U for up, D for down
        "code_recommend" : "undefined",
        "_GALLTYPE_" : "G", # G for gallery M for minor gallary 
        "link_id" : g_id
    }, headers={
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Origin': 'https://gall.dcinside.com',
        'Referer': f'https://gall.dcinside.com/board/view/?id={g_id}&no={g_no}',
    })
    sleep(SLEEP_INTERVAL)
    count -=1

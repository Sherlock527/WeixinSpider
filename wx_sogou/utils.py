# import urllib
from urllib.parse import urlencode, unquote


def gen_url(q_type, q_content, q_page):
    basic_url = "http://weixin.sogou.com/weixin"
    q_params = urlencode({"type": q_type, "page": q_page, "query": q_content})
    q_url = basic_url + "?" + q_params
    return q_url


def rm_highlight(filepath):
    html = open(filepath, "w")
    html_rm_highlight = html.read().replace("<em><!--red_beg-->", "").replace("<!--red_end--></em>", "")
    html.write(html_rm_highlight)
    html.close()

def stringToDict(cookie):
    itemDict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        itemDict[key] = value
    return itemDict


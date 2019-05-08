# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie':'_T_WM=7246b3dd258561730782b8b899a16ed5; SSOLoginState=1557326730; ALF=1559918730; SCF=Ahz5SB8HWCJDqkBjby56t0ad7l5136ICkIuli_Fe_MZlblks4OPuXflDfiVNXCR3lEw-OYI6l2XMsMsjzJGpfIA.; SUB=_2A25x1pvaDeRhGeVG6VIV-S7KyDqIHXVTOCWSrDV6PUNbktANLRDGkW1NT61cbYJqFNsiFL5P6gTpznSiV7mCLRzW; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFzinuuYvUQ32pM2gsDQigA5JpX5KzhUgL.FoeReo5X1K5ce0q2dJLoI7_edNSXIg4XIgUoU5tt; SUHB=0oUoK6odQaCzv1'
}

# CONCURRENT_REQUESTS 和 DOWNLOAD_DELAY 根据账号池大小调整 目前的参数是账号池大小为200

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 0.1

DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'sina.middlewares.CookieMiddleware': 300,
    'sina.middlewares.RedirectMiddleware': 200,
    'sina.middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'sina.pipelines.MongoDBPipeline': 300,
}

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'Sina'


# IP
DOWNLOAD_TIMEOUT = 10

RETRY_TIMES = 15

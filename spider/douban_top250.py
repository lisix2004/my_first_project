# 导入两个库
import re
import requests

# 请求头，地址
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0"}
url = "https://movie.douban.com/top250"

# 定义抓取网页函数
def fetch_page(url):
    response = requests.get(url=url, headers=headers)
    return response.text

# 定义匹配函数
def parse_page(html):
    pattern = re.compile(
            r'<span class="title">([^&nbsp].*?)</span>')
    movies = pattern.findall(html)
    return movies

html = fetch_page(url)
movies = parse_page(html)

# 抓取每一页
for page in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={page}"
    html = fetch_page(url)
    movies = parse_page(html)
    for movie in movies:
        print(f"{movie}")

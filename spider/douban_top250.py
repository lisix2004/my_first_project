import re
import requests

# 定义请求头，地址
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0"
}
base_url = "https://movie.douban.com/top250"

# 定义抓取网页函数
def fetch_page(url):
    response = requests.get(url=url, headers=headers)
    return response.text

# 定义匹配函数
def parse_page(html):
    pattern = re.compile(
        r'<span class="title">(.*?)</span>.*?'  # 匹配电影名称
        r'<span class="rating_num" property="v:average">(.*?)</span>',  # 匹配评分
        re.DOTALL
    )
    movies = pattern.findall(html)
    return movies

# 爬取每一页
for page in range(0, 250, 25):
    url = f"{base_url}?start={page}"
    html = fetch_page(url)
    movies = parse_page(html)

    # 打印结果
    for index, movie in enumerate(movies, start=page + 1):
        title = movie[0].strip()  # 去除空格
        rating = movie[1].strip()
        print(f"排名: {index}, 电影名称: {title}, 评分: {rating}")


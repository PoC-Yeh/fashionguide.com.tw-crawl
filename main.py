from bs4 import BeautifulSoup
import requests
from get_url import get_soup, urls, next_comment_page_url
from get_text import product, get_star_1, get_star_comment


url_list = []
#page
for i in range(1, 5):
    url ="http://shiseido.fashionguide.com.tw/search/beauty/?q=shiseido資生堂,資生堂,shiseido&p={}".format(i)
    urls(url)
    

new_url_list = []
soup = get_soup(test, "big5")

for i in range(0, len(url_list)):
    test = url_list[i]
    new_url_list.append(test)
    soup = get_soup(test, "big5")

    while True:
        next_page = next_comment_page_url(soup)
        if next_page != None:
            new_url_list.append(next_page)
            soup = get_soup(next_page, "big5")
        else:
            break

print(len(new_url_list))


#list of information, text of all pages
big_list = []

for i in range(0, len(new_url_list)):
    soup = get_soup(new_url_list[i], "big5")
    product_name = product(soup)
    star_unified = get_star_1(soup)
    comment_star = get_star_comment(soup)
    inside_list = [product_name, star_unified, comment_star]
    big_list.append(inside_list)
#print(big)


from bs4 import BeautifulSoup
import requests


def get_soup(url, encoding_type): #"utf-8", "big5"
    get_url = requests.get(url)
    get_url.encoding = encoding_type
    page = get_url.text
    soup = BeautifulSoup(page, "html.parser")
    return(soup)
    
    
def urls(url):          #urls in search result page
    soup = get_soup(url, "utf-8")
    #search result
    div = soup.find_all("div", class_="title")
    for i in div:
        div_a = i.find("a").get("href")
        url_list.append(div_a)
        
        
def next_comment_page_url(soup):
    td = soup.find_all("td", width= "100%", align = "right")[-1]
    fonts = td.find_all("font", class_ = "t9")
    font_list = []
    for font in fonts:
        font_list.append(font.text)
    a_tag = td.find_all("a")
    a_list= []
    for a in a_tag:
        a_list.append(a.get("href"))

    if '下一頁' in font_list and "下10頁" not in font_list:
        return("http://www.fashionguide.com.tw" + a_list[-1])
    elif '下一頁' in font_list and "下10頁" in font_list:
        return("http://www.fashionguide.com.tw" + a_list[-2])
        #print(a_list[-1])

        

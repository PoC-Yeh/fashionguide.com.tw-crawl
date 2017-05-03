from bs4 import BeautifulSoup
import requests


#product name
def product(soup):
    return(soup.find("span", class_= "style1", itemprop = "brand").text)
    

#回傳統整框格中的星等
def get_star_1(soup):
    all_star = soup.find_all("td", class_= "lin")
    star_info = []
    for i in all_star: 
        if i.find("img"):
            x = i.find("img")
            star_url = x.get("src")
            star_list = list(star_url)[-7:-4] #/s4, 4_5
            if star_list[0] == "/":
                star_info.append(int(star_list[-1])) #4
            else:
                star_info.append(float(".".join(("".join(star_list)).split("_"))))  #4.5
        else:
                star_info.append(i.text)
    #print(star_info) #['效果產生的速度', 4, '維持度', 4, '質地觸感', 4, '改善眼周細紋', 4, '吸收度', 4, '氣味', 4, '推展均勻度', 4.5]

    star_dict = {} 
    for i in range(0, len(star_info)):
        if i % 2 == 0 :
            star_dict[star_info[i]] = star_info[i + 1]
    return(star_dict) #{'效果產生的速度': 4, '質地觸感': 4, '維持度': 4, '吸收度': 4, '改善眼周細紋': 4, '氣味': 4, '推展均勻度': 4.5}
    
        
#回傳留言框格中的星等,user info
def get_star_comment(soup):
    tables = soup.find_all("table", class_= "t1", bgcolor = "#CCCCCC")
    star_dict_list = []
    for table in tables:
        all_star = table.find_all("td", valign = "top")
        #print(all_star)

        star_item = []
        star = []
        for i in all_star:
            font = i.find_all("font")
            for font_item in font:
                #print(font_item.text)
                star_item.append(font_item.text)


            img = i.find_all("img")
            for item in img:
                star_url = item.get("src")
                star_list = list(star_url)[-7:-4]
                if star_list[0] == "/":
                    star.append(int(star_list[-1])) #4
                    #print(int(star_list[-1]))
                else:
                    star.append(float(".".join(("".join(star_list)).split("_"))))  #4.5
                    #print(float(".".join(("".join(star_list)).split("_"))))


        star_info = {}
        for i in range(0, len(star)):
            star_info[star_item[i]] = star[i]
        #print(star_info)

        #user information
        user = table.find("td", bgcolor = "#ffffff", align = "left")
        if "滿意度" in user.text:
            user_text = user.text.replace("\xa0", "").replace("滿意度:(","").replace("分 / 滿分10分)年齡:",",").replace("皮膚屬性:",",")
            #['8', '36歲以上', '混合肌']
            star_info["point"] = int(user_text.split(",")[0]) #turn '8' into integer  
            age = user_text.split(",")[1]
            if "~" in age:
                age_low = "".join(list(age)[:2])
                star_info["age"] = int(age_low) + 2   #31~35 -->33 
            elif "以上" in age:
                star_info["age"] = "over"+ "".join(list(age)[:2]) #36歲以上-->over36
            if len(user_text.split(",")) == 3:   
                star_info["skin"] = user_text.split(",")[2]
        else:
            user_text = user.text.replace("\xa0", "").replace("年齡:",",").replace("皮膚屬性:",",")
            #[36歲以上', '混合肌']
            age = user_text.split(",")[0]
            if "~" in age:
                age_low = "".join(list(age)[:2])
                star_info["age"] = int(age_low) + 2   #31~35 -->33
            elif "以上" in age:
                star_info["age"] = "over"+ "".join(list(age)[:2]) #36歲以上-->over36
            star_info["skin"] = user_text.split(",")[1]

        
        star_dict_list.append(star_info)
    
    return(star_dict_list)
    
   

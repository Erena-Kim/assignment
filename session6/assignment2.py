import requests
from bs4 import BeautifulSoup
from assignment2_function import extract_info
import csv

# Making CSV
file = open("corona_hospital.csv", mode = "w", newline = "")
writer = csv.writer(file)
writer.writerow(["시도", "시군구", "선별진료소", "전화번호"])

# Extracting tag lists
node_html = requests.get("https://www.mohw.go.kr/react/popup_200128_3.html")
node_soup = BeautifulSoup(node_html.content, "html.parser", from_encoding = "utf-8") # 한글이 깨져서 이렇게 수정

# Extracting tbody tags
node_list_box = node_soup.find("tbody", {"class" : "tb_center"})

# Extracting tr tags
node_list = node_list_box.find_all("tr")

results = extract_info(node_list)

for result in results:
    row = []
    for i in result.keys():
        row.append(result[i])
    writer.writerow(row)

print("크롤링 끝!")
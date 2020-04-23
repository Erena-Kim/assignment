import requests
from bs4 import BeautifulSoup
from assignment1_function import extract_info
import csv

# Making CSV file
file = open("naver_books.csv", mode = "w", newline = "")
writer = csv.writer(file)
writer.writerow(["title", "img_src", "link", "author", "publisher", "price"])

final_result = []

#Extracting tag lists
for i in range(8): #8로 바꿔야 함
    print(f"{i+1}번째 크롤링 중...")
    note_html = requests.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")
    note_soup = BeautifulSoup(note_html.text, "html.parser")

    # Extracting ol tags
    note_list_box = note_soup.find("ol", {"class" : "basic"})

    # Extracting li tags
    note_list = note_list_box.find_all("li")

    # Extracting information
    result = extract_info(note_list)

    # Combining into list
    final_result += result

#Writing CSV
for result in final_result:
    row = []
    for i in result.keys():
        row.append(result[i])
    writer.writerow(row)

print("크롤링 끝!")

# note_html = requests.get("https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page=1")
# note_soup = BeautifulSoup(note_html.text, "html.parser")

#     # Extracting ol tags
# note_list_box = note_soup.find("ol", {"class" : "basic"})

#     # Extracting li tags
# note_list = note_list_box.find_all("li")

# title = note_list[0].find("a", {"class" : "N=a:bta.title"}).string
# print(title)
# img_src = note_list[0].find("img")["src"]
# print(img_src)
# link = note_list[0].find("a", {"class" : "N=a:bta.title"})["href"]
# print(link)
# author = note_list[0].find("a", {"class" : "txt_name N=a:bta.author"}).string.strip()
# print(author)
# publisher = note_list[0].find("a", {"class" : "N=a:bta.publisher"}).string
# print(publisher)
# price = note_list[0].find("em", {"class" : "price"}).string
# print(price)
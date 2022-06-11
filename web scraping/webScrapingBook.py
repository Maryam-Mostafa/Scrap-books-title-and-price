from selenium import webdriver
import csv

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/gp/bestsellers/books/")

titles = driver.find_elements_by_xpath("//div[@class='p13n-sc-truncated']")
prices = driver.find_elements_by_xpath("//span[@class='p13n-sc-price']")

for i in titles:
    print(i.text)

for i in prices:
    print(i.text)

with open("D:\Books.csv", "w", encoding="utf-8", newline="") as file:
    csvWriter = csv.writer(file, delimiter=",")
    csvWriter.writerow(["Title", "Price"])
    for i in range(1, len(titles)):
        csvWriter.writerow([titles[i].text, prices[i].text])

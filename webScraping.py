from selenium import webdriver
import csv

driver = webdriver.Chrome(r"D:\chromedriver_win32\chromedriver.exe")

driver.get("https://www.sos.ca.gov//state-holidays")

table = driver.find_elements_by_xpath("//div[@class='col-sm-12']")


for i in table:
    print(i.text)


'''with open("D:\table.csv", "w", encoding="utf-8", newline="") as file:
    csvWriter = csv.writer(file, delimiter=",")
    #csvWriter.writerow(["Title", "Price"])
    for i in range(1, len(table)):
        csvWriter.writerow(table[i].text)
'''
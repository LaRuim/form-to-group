import selenium_utils
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys 
import time
import csv

def main():
    driver = selenium_utils.make_driver()
    load = selenium_utils.load(driver)
    with open ("contact.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for line in csv_reader:
            if not line_count:
                line_count += 1
                continue
            print(f"Sending link to {line[1]} at {line[3]}")
            driver.get(f'https://web.whatsapp.com/send?phone=91{line[3]}')
            
            chat = load(r'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 'xpath')
            chat.send_keys("Join the I/O group here :)\nhttps://chat.whatsapp.com/BoR3W48hDDOE1JNfze8jzc") 
            time.sleep(2)
            chat.send_keys("\n")
    
main()
    
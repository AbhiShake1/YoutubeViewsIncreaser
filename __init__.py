from selenium import webdriver
from random import randint
from time import sleep


def init(url: str, number_of_views: int = 100):
    driver = webdriver.Chrome("chromedriver.exe")
    for i in range(number_of_views):
        driver.get(url)
        # to bypass youtube detection algorithm, pause randomly between 15 to 25 seconds
        # if youtube detects that the video is being watched for 10 seconds multiple times, it will be deleted
        sleep(randint(15, 25))

    driver.quit()  # close the browser


if __name__ == '__main__':
    init()

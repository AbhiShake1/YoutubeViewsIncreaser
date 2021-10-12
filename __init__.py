from selenium import webdriver
from random import randint
from time import sleep
from pyautogui import press


def init(url: str, number_of_views: int = 100):
    driver = webdriver.Chrome("chromedriver.exe")
    for i in range(number_of_views):
        driver.get(url)
        # let the url load
        sleep(1)
        if i == 0:
            press("space")  # only for the first time
        print(i, "times")
        # to bypass youtube detection algorithm, pause randomly between 5 to 15 seconds
        # if youtube detects that the video is being watched for 10 seconds multiple times, it will be deleted
        sleep(randint(5, 15))

    driver.quit()  # close the browser


if __name__ == '__main__':
    init(
        "https://youtu.be/XX9lMxscBS0",  # url
        100000,  # number of views
    )

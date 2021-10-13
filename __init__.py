def init(url: str, number_of_views: int = 100, number_of_sessions: int = 1):
    from selenium import webdriver
    from random import randint
    from time import sleep
    from pyautogui import press
    drivers = []
    [drivers.append(webdriver.Chrome("chromedriver.exe")) for _ in range(number_of_sessions)]
    # driver = webdriver.Chrome("chromedriver.exe")
    for i in range(number_of_views):
        [driver.get(url) for driver in drivers]
        # let the url load
        sleep(1)
        if i == 0:
            press("space")  # only for the first time
        print(i + 1, "times")
        # to bypass youtube detection algorithm, pause randomly between 2 to 4 seconds (probably unsafe but i am
        # just testing with fastest possible values)
        # if youtube detects that the video is being watched for 10 seconds multiple times, it will be deleted
        sleep(randint(2, 4))
    exit()  # close the browser and program after method execution completes


if __name__ == '__main__':
    init(
        "https://youtu.be/XX9lMxscBS0",  # url
        100000,  # number of views/ number of times the program will run
        4,  # number of sessions (more sessions, faster increase in views)
    )

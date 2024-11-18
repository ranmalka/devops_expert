import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_score_service():
    # Initialize the WebDriver (using Chrome in this example)

    # WebDriver setup
    opt = webdriver.ChromeOptions()
    opt.add_argument('ignore-certificate-errors')
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=opt)

    constructed_path = 'http://localhost:8777'

    print(f"Constructed path: {constructed_path}")
    try:
        driver.get(constructed_path)
        driver.implicitly_wait(10)
        score = driver.find_element(By.ID, "score").text
        if 1 <= int(score) <= 1000:
            return True
        else:
            return False
    except:
        return False

def test_score_main():
    if test_score_service() == True:
        exit(0)
    else:
        exit(-1)

test_score_main()
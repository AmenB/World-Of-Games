import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Fixed import
from selenium import webdriver
from selenium.webdriver.common.by import By
import re  # Import for regex

def test_scores_service():
    chrome_options = Options()  # Use Options for Chrome-specific options

    # Initialize the WebDriver
    service = Service(ChromeDriverManager().install())
    driver_chrome = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver_chrome.get("http://127.0.0.1:8777/")
        score_element = driver_chrome.find_element(By.ID, "score")
        score_text = score_element.text  # Get the text of the element

        # Extract the number using regex
        match = re.search(r'\d+', score_text)
        if match:
            score = int(match.group())  # Convert the extracted number to an integer
            if 0 <= score <= 1000:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver_chrome.quit()  # Ensure WebDriver is closed even if an error occurs

def main_function():
    if test_scores_service():
        sys.exit(0)
    else:
        sys.exit(-1)

if __name__ == "__main__":
    main_function()

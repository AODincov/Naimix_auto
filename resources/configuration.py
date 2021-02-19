import os
import platform

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if platform.system() == "Linux":
    CHROME_PATH = os.path.join(BASE_DIR, "resources", "chromedriver")
elif platform.system() == 'Windows':
    CHROME_PATH = os.path.join(BASE_DIR, "resources", "chromedriver.exe")

TIMEOUT = 60

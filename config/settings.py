from pathlib import Path

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php"
LOGIN_URL = BASE_URL+"/auth/login"
DEFAULT_TIMEOUT = 20000
BASE_DIR = Path(__file__).resolve().parent.parent

ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"

FIRST_NAME = "Gamnishko"
MIDDLE_NAME = "GamnoMiddleName"
LAST_NAME = "GamnoLastName"
EMPLOYEE_ID = "1489"
USERNAME = "JoePeach"
PASSWORD = "qwerty123"
TEST_IMAGES_DIR = BASE_DIR/'helpers'/'data'/'test_images'
TEST_IMAGE_PATH = TEST_IMAGES_DIR/'valid_test_image.jpg'

PIM_ADD_EMPLOYEE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"
PIM_EMPLOYEE_LIST_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"


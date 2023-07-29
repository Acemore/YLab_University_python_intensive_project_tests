import dotenv
import os

dotenv.load_dotenv()

LOCAL_URL = os.getenv('LOCAL_URL')
APP_ROOT_URL = f'{LOCAL_URL}/api/v1/menus'

DISH_1_DATA_TO_CREATE_FILE_PATH = './tests/fixtures/dish_1_data_to_create.json'
DISH_1_DATA_TO_UPDATE_FILE_PATH = './tests/fixtures/dish_1_data_to_update.json'
DISH_2_DATA_TO_CREATE_FILE_PATH = './tests/fixtures/dish_2_data_to_create.json'
DISH_2_DATA_TO_UPDATE_FILE_PATH = './tests/fixtures/dish_2_data_to_update.json'
MENU_DATA_TO_CREATE_FILE_PATH = './tests/fixtures/menu_data_to_create.json'
MENU_DATA_TO_UPDATE_FILE_PATH = './tests/fixtures/menu_data_to_update.json'
SUBMENU_DATA_TO_CREATE_FILE_PATH = './tests/fixtures/submenu_data_to_create.json'
SUBMENU_DATA_TO_UPDATE_FILE_PATH = './tests/fixtures/submenu_data_to_update.json'

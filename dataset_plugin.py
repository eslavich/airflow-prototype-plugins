from airflow.plugins_manager import AirflowPlugin

MENU_ITEM = {
    "name": "Google",
    "category": "Search",
    "category_icon": "fa-th",
    "href": "https://www.google.com"
}

class DatasetPlugin(AirflowPlugin):
    name = "Dataset Plugin"

    appbuilder_menu_items = [MENU_ITEM]
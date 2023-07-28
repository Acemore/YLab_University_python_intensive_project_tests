import requests
# from unittest import TestCase

from tests import LOCAL_URL

empty_menus_list = []
menu_data_to_create = {
    'title': 'title_to_create',
    'description': 'description_to_create',
}
menu_id = None
menu_data_to_update = {
    'title': 'updated_title',
    'description': 'updated_description',
}


def test_read_empty_menus_list():
    empty_menus_list_resp = requests.get(f'{LOCAL_URL}/api/v1/menus')

    assert empty_menus_list_resp.status_code == 200
    assert empty_menus_list_resp.json() == empty_menus_list


def test_create_menu():
    created_menu_resp = requests.post(f'{LOCAL_URL}/api/v1/menus/', json=menu_data_to_create)
    resp_json = created_menu_resp.json()

    assert created_menu_resp.status_code == 201
    assert resp_json['title'] == menu_data_to_create['title']
    assert resp_json['description'] == menu_data_to_create['description']


def test_read_menus_list():
    menus_list_resp = requests.get(f'{LOCAL_URL}/api/v1/menus')
    resp_json = menus_list_resp.json()

    assert menus_list_resp.status_code == 200
    assert resp_json != empty_menus_list


def test_read_menu():
    menus_list_resp = requests.get(f'{LOCAL_URL}/api/v1/menus')
    menus = menus_list_resp.json()
    menu = menus[0]
    global menu_id
    menu_id = menu['id']

    menu_resp = requests.get(f'{LOCAL_URL}/api/v1/menus/{menu_id}')
    menu = menu_resp.json()

    assert menu_resp.status_code == 200
    assert menu['title'] == menu_data_to_create['title']
    assert menu['description'] == menu_data_to_create['description']


def test_update_menu():
    global menu_id
    menu_resp = requests.get(f'{LOCAL_URL}/api/v1/menus/{menu_id}')
    menu = menu_resp.json()

    assert menu['title'] == menu_data_to_create['title']
    assert menu['description'] == menu_data_to_create['description']

    updated_menu_resp = requests.patch(
        f'{LOCAL_URL}/api/v1/menus/{menu_id}',
        json=menu_data_to_update,
    )
    updated_menu = updated_menu_resp.json()

    assert updated_menu_resp.status_code == 200
    assert updated_menu['title'] == menu_data_to_update['title']
    assert updated_menu['description'] == menu_data_to_update['description']


def test_read_updated_menu():
    global menu_id

    retrieved_updated_menu_resp = requests.get(f'{LOCAL_URL}/api/v1/menus/{menu_id}')
    retrieved_updated_menu = retrieved_updated_menu_resp.json()

    assert retrieved_updated_menu_resp.status_code == 200
    assert retrieved_updated_menu['title'] == menu_data_to_update['title']
    assert retrieved_updated_menu['description'] == menu_data_to_update['description']


def test_delete_menu():
    global menu_id
    resp = requests.delete(f'{LOCAL_URL}/api/v1/menus/{menu_id}')

    assert resp.status_code == 200
    assert resp.json() == {'ok': True}


def test_read_menus_list_after_deleting():
    menus_list_resp = requests.get(f'{LOCAL_URL}/api/v1/menus')

    assert menus_list_resp.status_code == 200
    assert menus_list_resp.json() == empty_menus_list


def test_read_deleted_menu():
    global menu_id
    resp = requests.get(f'{LOCAL_URL}/api/v1/menus/{menu_id}')

    assert resp.status_code == 404
    print(resp.__dict__)
    assert resp.json()['detail'] == 'menu not found'

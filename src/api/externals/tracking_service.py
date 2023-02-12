from typing import Union
from urllib.parse import urljoin

import requests
from requests.exceptions import RequestException

TRACKING_SERVICE_URL = 'https://app-tracking.azurewebsites.net/v1/'


def get_places(place_type: Union[str, None]):
    """所在の一覧を取得する

    Args:
        place_type (str): 所在タイプ
    """
    url = urljoin(TRACKING_SERVICE_URL, 'place/')

    try:
        if not place_type:
            res = requests.get(url)
        else:
            res = requests.get(url, params={"place_type": place_type})

        return res.json()
    except RequestException as e:
        print(e.response.text)
        raise e


def get_place_by_id(place_id: str):
    """所在をIDで取得する

    Args:
        place_id (str): 所在ID

    Raises:
        e: RequestException

    Returns:
        dict: json
    """
    url = urljoin(TRACKING_SERVICE_URL, 'place/')
    url = urljoin(url, place_id)

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()

    except RequestException as e:
        print(e.response.text)
        raise e


def get_place_by_tank(tank_id: str):
    """タンクIDから、そのタンクがある所在のIDと名称を取得する

    Args:
        tank_id (str): タンクID

    Raises:
        e: RequestException

    Returns:
        _type_: json
    """
    url = urljoin(TRACKING_SERVICE_URL, 'tank/')
    url = urljoin(url, tank_id + '/')
    url = urljoin(url, 'place')

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()

    except RequestException as e:
        print(e.response.text)
        raise e


def get_tanks(place_id: str):
    """所在IDでタンク一覧を取得する

    Args:
        place_id (str): 所在ID

    Raises:
        e: RequestException

    Returns:
        _type_: json
    """
    url = urljoin(TRACKING_SERVICE_URL, 'place/')
    url = urljoin(url, place_id + '/')
    url = urljoin(url, 'tanks')

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()

    except RequestException as e:
        print(e.response.text)
        raise e


def get_tank(place_id: str, tank_id: str):
    """タンクを取得する

    Args:
        place_id (str): 所在ID （所在とタンクはデータ上は親子関係はないが、理論上は親子なので指定する）
        tank_id (str): タンクID

    Raises:
        e: RequestException

    Returns:
        _type_: json
    """
    url = urljoin(TRACKING_SERVICE_URL, 'tank/')
    url = urljoin(url, tank_id + '/')

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()

    except RequestException as e:
        print(e.response.text)
        raise e


def get_tank_name(place_id: str, tank_id: str):
    """タンク名称を取得する

    Args:
        place_id (str): 所在ID
        tank_id (str): タンクID

    Returns:
        str: タンク名称
    """
    try:
        res = get_tanks(place_id)

        list_tank = list(filter(lambda x: x['tank_id'] == tank_id, res))

        return list_tank[0]['tank_name'] if len(list_tank) == 1 else ''

    except RequestException:
        return ''


def get_tank_vol(place_id: str, tank_id: str) -> float:
    """タンク名称とタンク容量を取得する

    Args:
        place_id (str): 所在ID
        tank_id (str): タンクID

    Returns:
        str: タンク容量
    """
    DEFAULT_TANK_VOL: float = 100000

    try:
        res = get_tanks(place_id)

        list_tank = list(filter(lambda x: x['tank_id'] == tank_id, res))
        if len(list_tank) == 1:
            return list_tank[0]['tank_vol']
        else:
            return DEFAULT_TANK_VOL

    except RequestException:
        return DEFAULT_TANK_VOL


def get_place_id_and_name_by_tank(tank_id: str) -> tuple[str, str]:
    """タンクIDから、そのタンクがある所在のIDと名称を取得する

    Args:
        tank_id (str): タンクID

    Returns:
        tuple[str, str]: 所在ID, 所在名称
    """
    try:
        r = get_place_by_tank(tank_id)

        return (r['place_id'], r['place_name'])

    except RequestException:
        return '', ''

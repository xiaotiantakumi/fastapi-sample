import math
from urllib.parse import urljoin

import requests
from requests.exceptions import RequestException

HYDROGEN_SERVICE_URL = 'https://app-hydrogen.azurewebsites.net/v1/'


def get_hydrogen(hydrogen_id: str):
    """データ管理サービスから水素を取得する

    Args:
        hydrogen_id (str): 水素ID

    Raises:
        e: RequestException

    Returns:
        dict: 水素
    """
    url = urljoin(HYDROGEN_SERVICE_URL, 'he/')
    url = urljoin(url, hydrogen_id)

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()[0]

    except RequestException as e:
        print(e.response.text)
        raise e


def get_hydrogens_in_the_tank(tank_id: str):
    """タンクに入っている水素の一覧を取得する

    Args:
        tank_id (str): タンクID

    Raises:
        e: RequestException

    Returns:
        list[dict]: 水素のリスト
    """
    url = urljoin(HYDROGEN_SERVICE_URL, 'he/tank/')
    url = urljoin(url, tank_id)

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()

    except RequestException as e:
        print(e.response.text)
        raise e


def get_trace(hydrogen_id: str) -> list[dict]:
    """水素データ管理サービスから水素のトレース情報を取得する

    Args:
        hydrogen_id (str): 水素ID

    Raises:
        e: RequestException

    Returns:
        _type_: トレース情報のリスト
    """

    url = urljoin(HYDROGEN_SERVICE_URL, 'he/')
    url = urljoin(url, hydrogen_id + '/')
    url = urljoin(url, 'trace')

    try:
        # TODO データ管理サービス側のlimitの指定が固定されている
        r = requests.get(url, params={"hydrogen_id": hydrogen_id})
        r.raise_for_status()

        return r.json()

    except RequestException as e:
        print(e.response.text)
        raise e


def calc_emission_intensity(e: float, v: float) -> float:
    """emission intensity（CO2-g/H2-Nm3）の計算
       emissionの値は、staticとvariableのemissionの和
       (表示する低炭素価値) = (staticとvariableのemissionの和) x 1000000 ÷ (staticとvariableのvolumeの和)
       小数点2桁表示（3桁目を切り捨て）

    Args:
        e (float): CO2-t
        v (float): H2-Nm3

    Returns:
        float: CO2-g/H2-Nm3
    """
    if v == 0:
        return 0

    return math.floor(e * 1000000 / v * 100) / 100

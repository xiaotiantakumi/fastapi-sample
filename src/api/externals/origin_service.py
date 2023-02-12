from urllib.parse import urljoin

import requests
from requests.exceptions import RequestException

ORIGIN_SERVICE_URL = 'https://app-origin-go.azurewebsites.net/v1/'


def get_origin(go_id: str):
    """水素の原産地証明を取得する

    Args:
        go_id (str): GOのID

    Raises:
        e: RequestException

    Returns:
        _type_: json
    """
    url = urljoin(ORIGIN_SERVICE_URL, 'origin/')
    url = urljoin(url, go_id)

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()

    except RequestException as e:
        print(e.response.text)
        raise e

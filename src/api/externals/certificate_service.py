from urllib.parse import urljoin

import requests
from requests.exceptions import RequestException


CERTIFICATE_SERVICE_URL = 'https://app-certificate.azurewebsites.net/v1/'


def get_certificate(certificate_id: str):
    """証書管理サービスから証書を取得する

    Args:
        certificate_id (str): 証書ID

    Raises:
        e: RequestException

    Returns:
        _type_: json
    """
    url = urljoin(CERTIFICATE_SERVICE_URL, 'certificate/')
    url = urljoin(url, certificate_id)

    try:
        r = requests.get(url)
        r.raise_for_status()

        return r.json()

    except RequestException as e:
        print(e.response.text)
        raise e

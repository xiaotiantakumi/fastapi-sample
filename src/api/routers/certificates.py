import datetime

from fastapi import APIRouter
from requests.exceptions import RequestException

import api.externals.certificate_service as certificate_service
import api.externals.hydrogen_service as hydrogen_service
import api.externals.dummy_data_service as dummy_data_service
import api.externals.tracking_service as tracking_service
import api.schemas.certificate as certificate_schema

router = APIRouter(tags=["Certificates"])


@router.get("/certificates/{certificate_id}", response_model=certificate_schema.GetCertificateResponse)
async def get_certificates(certificate_id: str):

    try:
        # 証書サービスから証書を取得
        r = certificate_service.get_certificate(certificate_id)

        # 所在名称取得
        res = tracking_service.get_places(None)
        list_place = list(filter(lambda x: x['place_id'] == r['last_place_id'], res))
        place_name = list_place[0]['place_name'] if len(list_place) == 1 else ''

        # オーナー名の取得
        owner_neme = dummy_data_service.get_owner_name(r['last_owner_id'])

        use_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

        # emission intensity（CO2-g/H2-Nm3）の計算
        emission_intensity = hydrogen_service.calc_emission_intensity(
            r['emission'], r['volume'])

        return certificate_schema.GetCertificateResponse(
            **r,
            last_place_name=place_name,
            last_owner_name=owner_neme,
            production_method='LIGNITE',
            date_of_issue=use_time,
            date_of_use=use_time,
            emission_intensity=emission_intensity,
        )

    except RequestException as e:
        print(e.response.text)
        raise e

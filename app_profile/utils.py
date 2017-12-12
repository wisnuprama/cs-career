import requests
from app_auth import utils as auth_utils

API_URL = {
    'linkedin': '',
    'profile': 'https://private-e52a5-ppw2017.apiary-mock.com/riwayat'
}


def __get_riwayat__(user=None):
    resp = requests.get(url=API_URL['profile'])
    return resp.json()


def get_query_user_history(npm):
    user = auth_utils.get_or_create_user(npm=npm)
    hist = __get_riwayat__(user)

    result = []
    for mk in hist:
        res = dict()
        res['kode_mk'] = mk.get('kd_mk')
        res['tahun'] = mk.get('tahun')

        data_mk = mk.get('kelas')
        if data_mk:
            data_mk = data_mk.get('nm_mk_cl')
            res['nama_mk'] = data_mk.get('nm_mk')
            res['jml_sks'] = data_mk.get('jml_sks')
        res['nilai'] = mk.get('nilai') if user.is_showing_score else 'Dirahasiakan'

        result.append(res)

    return result

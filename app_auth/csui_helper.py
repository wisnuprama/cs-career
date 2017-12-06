import requests

API_MAHASISWA = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
API_VERIFY_USER = "https://akun.cs.ui.ac.id/oauth/token/verify/"


def get_access_token(username, password):
    try:
        url = "https://akun.cs.ui.ac.id/oauth/token/"

        payload = "username=" + username + "&password=" + password + "&grant_type=password"
        headers = {
            'authorization': "Basic WDN6TmtGbWVwa2RBNDdBU05NRFpSWDNaOWdxU1UxTHd5d3U1V2VwRzpCRVFXQW43RDl6a2k3NEZ0bkNpWVhIRk50Ymg3eXlNWmFuNnlvMU1uaUdSVWNGWnhkQnBobUU5TUxuVHZiTTEzM1dsUnBwTHJoTXBkYktqTjBxcU9OaHlTNGl2Z0doczB0OVhlQ3M0Ym1JeUJLMldwbnZYTXE4VU5yTEFEMDNZeA==",
            'cache-control': "no-cache",
            'content-type': "application/x-www-form-urlencoded"
        }
        response = requests.request("POST", url, data=payload, headers=headers)

        return response.json()["access_token"]
    except Exception as e:
        return None
        # raise Exception("username atau password sso salah, input : [{}, {}]".format(username, password,))


def get_client_id():
    CLIENT_ID = 'X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG'
    return CLIENT_ID


def verify_user(access_token):
    parameters = {"access_token": access_token, "client_id": get_client_id()}
    response = requests.get(API_VERIFY_USER, params=parameters)
    return response.json()


def get_data_user(access_token, id):
    parameters = {"access_token": access_token, "client_id": get_client_id()}
    response = requests.get(API_MAHASISWA + id, params=parameters)
    return response.json()

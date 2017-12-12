from app_profile import utils as profile_utils


def index(request, data):
    user_npm = request.session['user_login']['npm']

    # data profile
    data['user_riwayat'] = profile_utils.get_query_user_history(user_npm)

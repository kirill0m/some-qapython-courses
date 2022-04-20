from models.models import MostCommonMethodsModel
from models.models import MostCommonRequestsModel
from models.models import MostCommonUsersServerErrorModel
from models.models import BiggestRequestsClientError


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_mc_method(self, method=None, count=None):
        method = method
        count = count

        mc_method = MostCommonMethodsModel(
            method=method,
            count=count
        )
        self.client.session.add(mc_method)
        self.client.session.commit()

        return mc_method

    def create_mc_req(self, request=None, count=None):
        request = request
        count = count

        mc_request = MostCommonRequestsModel(
            request=request,
            count=count
        )
        self.client.session.add(mc_request)
        self.client.session.commit()

        return mc_request

    def create_mc_user_srverror(self, user=None, count=None):
        user = user
        count = count

        mc_user_srverror = MostCommonUsersServerErrorModel(
            user=user,
            count=count
        )

        self.client.session.add(mc_user_srverror)
        self.client.session.commit()

        return mc_user_srverror

    def create_bgst_req_clienterror(self, user, request, status, size):
        user = user
        request = request
        status = status
        size = size

        bgst_req_clienterror = BiggestRequestsClientError(
            user=user,
            request = request,
            status = status,
            size = size,
        )

        self.client.session.add(bgst_req_clienterror)
        self.client.session.commit()

        return bgst_req_clienterror

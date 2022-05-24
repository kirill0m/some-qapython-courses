import pytest
from base import Base

class TestsMySQL(Base):
    @pytest.mark.parametrize('top, exp_method_count', [(4, 4)])
    def test_mc_methods(self, items_from_logs, top, exp_method_count):
        self.insert_mc_methods(items_from_logs, top)
        res = self.select_mc_methods()
        assert len(res) == exp_method_count if top > exp_method_count else top

    @pytest.mark.parametrize('top', [10])
    def test_mc_requests(self, items_from_logs, top):
        self.insert_mc_requests(items_from_logs, top)
        res = self.select_mc_requests()
        assert len(res) == top

    @pytest.mark.parametrize('top', [5])
    def test_mc_users_srverror(self, items_from_logs, top):
        self.insert_mc_users_srverror(items_from_logs, top)
        res = self.select_mc_users_srverror()
        assert len(res) == top

    @pytest.mark.parametrize('top', [10])
    def test_bgst_reqs_clienterror(self, items_from_logs, top):
        self.insert_bgst_reqs_clienterror(items_from_logs, top)
        res = self.select_bgst_reqs_clienterror()
        assert len(res) == top
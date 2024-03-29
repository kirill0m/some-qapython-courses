import pytest
from base import ApiBase


class TestsLogin(ApiBase):
    @pytest.mark.API
    def test_login(self):
        expected_url = self.api_client.session.get(url='https://target.my.com').url
        assert expected_url == 'https://target.my.com/dashboard'


class TestsCampaign(ApiBase):
    @pytest.mark.API
    def test_create_campaign(self):
        campaign_data = self.builder.campaign()
        campaign_id = self.api_client.post_create_campaign(campaign_data.name, campaign_data.objective,
                                                           campaign_data.package_id)
        resp = self.api_client.get_campaign_by_id(campaign_id)
        assert resp['name'] == campaign_data.name


class TestsSegment(ApiBase):
    @pytest.mark.API
    def test_create_segment(self):
        segment_data = self.builder.segment()
        segment_id = self.api_client.post_create_segment(segment_data.name, segment_data.pass_condition,
                                                         segment_data.relations, segment_data.logicType)
        res = self.api_client.get_segment_by_id(segment_id)

        assert res['name'] == segment_data.name

    @pytest.mark.API
    def test_delete_segment(self):
        segment_data = self.builder.segment()
        segment_id = self.api_client.post_create_segment(segment_data.name, segment_data.pass_condition,
                                                         segment_data.relations, segment_data.logicType)

        assert self.api_client.delete_segment_by_id(segment_id)

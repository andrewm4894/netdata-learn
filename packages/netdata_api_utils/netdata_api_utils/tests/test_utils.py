from netdata_api_utils.utils import api, get_metrics

def test_api_has_mirrored_hosts():
    # test api pulls back at least some mirrored_hosts
    assert len(api()['mirrored_hosts'])>=1

    
def test_get_metrics_has_rows():
    # test you get some rows from calling get_metrics()
    assert get_metrics().shape[0]>=1
    

def test_get_metrics_has_expected_cols():
    # test you get expected number of cols
    assert get_metrics().shape[1]==4

def do_fail():
    assert 1==0
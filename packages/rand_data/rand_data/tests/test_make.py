from rand_data.make import make_data

def test_make_data():
    df = make_data()
    assert df.shape[0]==1250
    assert df.shape[1]==6

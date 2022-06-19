import pytest
from utilities.util import Util

# ***************** DATA *****************
additional_data = [
        ('pawel.automatyzacja@gmail.com', 'haslotestowe', Util.generate_email()),
        ('pawel.a.utomatyzacja@gmail.com', 'haslotestowe', Util.generate_email())
        ]


@pytest.fixture(params=additional_data, scope="class")
def data_load(request):
    return request.param

import pytest

from masqstat import web
from tempfile import NamedTemporaryFile

TEST_DNSMASQ_FILE = """1588732044 00:18:dd:04:40:d4 10.9.1.21 hdhomerun 01:00:18:dd:04:40:d4
1588731863 18:b4:30:ea:33:c3 10.9.2.170 Nest-Hello-33c3 01:18:b4:30:ea:33:c3
1588730578 98:da:c4:04:36:c1 10.9.2.116 HS100 01:98:da:c4:04:36:c1

"""


@pytest.fixture
def client():
    with NamedTemporaryFile() as f:
        f.file.write(TEST_DNSMASQ_FILE.encode('ascii'))
        f.file.flush()
        web.app.config['lease_file'] = f.name
        yield web.app.test_client()


def test_root(client):
    rv = client.get('/')
    assert rv.status_code == 200

    for val in ['Nest-Hello-33c3', '10.9.2.116']:
        assert val in rv.data.decode('utf-8')

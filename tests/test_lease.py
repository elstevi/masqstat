import ipaddress
import pytest
from masqstat.lease import Lease


def test_load_lease():
    line = '1588732146 b8:2c:a0:81:54:8a 10.9.1.136 Gateway81548A b8:2c:a0:81:54:8b'
    mylease = Lease(line=line)
    assert mylease.mac1 == 'b8:2c:a0:81:54:8a'
    assert mylease.mac2 == 'b8:2c:a0:81:54:8b'
    assert mylease.hostname == 'Gateway81548A'
    assert mylease.ip == ipaddress.ip_address('10.9.1.136')


def test_no_mac2():
    line = '1588732146 b8:2c:a0:81:54:8a 10.9.1.136 Gateway81548A *'
    mylease = Lease(line=line)
    assert mylease.mac2 is None


def test_bad_line():
    line = 'this is some junk'
    with pytest.raises(TypeError):
        Lease(line=line)

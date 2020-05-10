import pytest

from masqstat.utils import load_lease_file
from masqstat.lease import Lease
from tempfile import NamedTemporaryFile

EXAMPLE_LEASE_FILE = """1588730584 b4:f1:da:e8:c8:cd 10.9.1.135 * 01:b4:f1:da:e8:c8:cd
1588732572 64:bc:0c:51:5e:0e 10.9.2.194 * 01:64:bc:0c:51:5e:0e
1588730005 a8:a7:95:36:54:c5 10.9.2.113 BrotherPrinter5 01:a8:a7:95:36:54:c5
1588731322 b8:a1:75:86:87:cb 10.9.1.191 * *
1588729368 98:f2:b3:14:fa:0a 10.9.1.23 plex 01:98:f2:b3:14:fa:0a
1588730659 44:07:0b:77:cf:6f 10.9.1.150 Chromecast *
1588732401 c4:2a:d0:e3:f4:5b 10.9.1.174 iPad 01:c4:2a:d0:e3:f4:5b

"""


def test_load_leases():
    with NamedTemporaryFile() as f:
        f.file.write(EXAMPLE_LEASE_FILE.encode('ascii'))
        f.file.flush()
        leases = load_lease_file(f.name)
        for lease in leases:
            assert isinstance(lease, Lease)


def test_load_bad_leases():
    with pytest.raises(IOError):
        load_lease_file('/dev/null')

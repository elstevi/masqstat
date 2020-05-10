import datetime
import ipaddress
import re

from netaddr import EUI
from netaddr.core import NotRegisteredError


class Lease:
    """ Class that represents a single dnsmasq lease.

    Args:
        line (str): a line from a dnsmasq state file.
    """
    def __init__(self, line=None):
        self.lease_time = None
        self.mac1 = None
        self.mac2 = None
        self.ip = None
        self.hostname = None

        if line:
            self.parse(line)

    def mac_to_manufacturer(self):
        try:
            oui_info = EUI(self.mac1).oui.registration().org
        except (NotRegisteredError, TypeError):
            oui_info = ''
        return oui_info

    def parse(self, line):
        """ Parse a dnsmasq state file line.

        Args:
            line (str): a line from a dnsmasq state file.
        """
        pattern = ('(?P<lease_time>[0-9]+) (?P<mac1>[a-f0-9\\:]{17}) (?P<ip>[0-9a-f.]+) (?P<hostname>.+) (?P<mac2>.+)')
        res = re.match(pattern, line)
        if hasattr(res, 'groupdict'):
            m = res.groupdict()
            lease_time = datetime.datetime.fromtimestamp(int(m.get('lease_time')))
            ip = ipaddress.ip_address(m.get('ip'))
            mac1 = m.get('mac1')
            oui_info = self.mac_to_manufacturer()

            if m.get('mac2') and m.get('mac2') != '*':
                mac2 = m.get('mac2')
            else:
                mac2 = None

            f = {
                'lease_time': lease_time,
                'ip': ip,
                'mac1': mac1,
                'mac2': mac2,
                'hostname': m.get('hostname'),
                'manufacturer': oui_info,
            }
            self.__dict__.update(f)
        else:
            raise TypeError('Invalid input line')

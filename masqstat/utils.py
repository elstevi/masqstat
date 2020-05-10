import logging

from os.path import isfile
from masqstat.lease import Lease

logger = logging.getLogger('utils')


def load_lease_file(lease_file):
    """ Load leases into objects from filesystem.

        Uses:
            app.config['lease_file']

    """
    if not isfile(lease_file):
        raise IOError('File not found: {}'.format(lease_file))

    with open(lease_file) as f:
        lines = f.readlines()
    leases = []
    for line in lines:
        try:
            new = Lease(line=line)
            leases.append(new)
        except TypeError:
            logging.warning('Throwing away lease created from line %s', line)
    return leases

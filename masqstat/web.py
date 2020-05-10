import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_table import Table, Col
from masqstat.utils import load_lease_file


app = Flask(__name__)
Bootstrap(app)
app.config.update(
    lease_file=os.environ.get('MASQSTAT_LEASE_FILE'),
    BOOTSTRAP_SERVE_LOCAL=True,
)


class ItemTable(Table):  # pylint: disable=abstract-method
    """ Schema for table """
    mac1 = Col('MAC')
    ip = Col('IP Address')
    hostname = Col('Hostname')
    manufacturer = Col('Manufacturer')
    lease_time = Col('Last seen')
    classes = ['table', 'table-striped']
    thead_classes = ['thead-dark']


@app.route('/')
def home():
    """ flask main page view """
    leases = load_lease_file(app.config.get('lease_file'))
    final_leases = []
    for lease in leases:
        final_leases.append(lease.__dict__)
    table = ItemTable(final_leases)

    return render_template('home.html', body=table.__html__()), 200

========
Starting
========

To start with gunicorn:

.. code-block:: bash

   gunicorn -b 0.0.0.0:8000 masqstat.web:app

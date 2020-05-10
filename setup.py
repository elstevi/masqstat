from setuptools import setup

setup(
    name='masqstat',
    version='0.1',
    install_requires=[
        'datetime',
        'flask',
        'flask_bootstrap',
        'flask_table',
        'gunicorn',
        'netaddr',
        'requests',
    ],
    extras_require={
        'dev': [
            'ipython',
            'ipdb',
            'sphinx',
            'sphinx_rtd_theme',
        ],
        'test': [
            'pytest',
            'pytest-cov',
            'pylint',
        ]
    },
)

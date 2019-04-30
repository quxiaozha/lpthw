try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
'description': 'Learn Python the hard way',
'author': 'quxiaozha',
'url': 'https://github.com/quxiaozha',
'download_url': 'https://github.com/quxiaozha',
'author_email': 'quxun1992@126.com',
'version': '0.1',
'install_requires': ['nose', 'lpthw-web'],
'packages': ['lpthw'],
'scripts': [],
'name': 'learn-py-the-hard-way'
}
setup(**config)

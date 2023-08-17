from distutils.core import setup

setup(name='socksimap',
    version='1.0.0',
    description='Connect to IMAP through Socks',
    install_requires=["PySocks"],
    author='optinsoft',
    author_email='optinsoft@gmail.com',
    keywords=['socks','imap'],
    url='https://github.com/optinsoft/socksimap',
    packages=['socksimap']
)
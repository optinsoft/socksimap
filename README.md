# Connect to IMAP through Socks

## Dependencies

- PySocks 1.7.1+

## Installation

```bash
pip install socksimap
```

or

```bash
pip install git+https://github.com/optinsoft/socksimap.git
```

## Usage

```python
from socksimap import SocksIMAP4_SSL

email_address = 'YOUR_ACCOUNT@hotmail.com'
password = 'YOUR_PASSWORD'
imap_server = 'outlook.office365.com'
imap_port = 993
socks_addr = '127.0.0.1'
socks_port = 1080
socks_type = 'socks5'

imap = SocksIMAP4_SSL(host=imap_server, port=imap_port, timeout=15,
                      proxy_addr=socks_addr, proxy_port=socks_port, proxy_type=socks_type)
imap.login(email_address, password)
imap.logout()

```

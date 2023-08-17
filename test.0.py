from imaplib import IMAP4
import email
from email.header import decode_header
from socksimap import SocksIMAP4_SSL

def print_inbox(imap: IMAP4, top: int = 5):
    # some code from the article "How to Read Emails in Python":
    # https://thepythoncode.com/article/reading-emails-in-python
    status, messages = imap.select("INBOX")
    messages = int(messages[0])
    print(f"status:   {status}")
    print(f"messages: {messages}")
    print(f"top {top}:")
    for i in range(messages, messages-top, -1):
        if i < 1: break
        res, msg = imap.fetch(str(i), "(RFC822)")
        print(f"res[{i}]: {res}")
        print(f"message[{i}]:")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]     
                if isinstance(From, bytes):
                    From = From.decode(encoding)      
                print(f"Subject: {subject}")
                print(f"From: {From}")
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain":
                            # print text/plain part
                            print(body)
                        if content_type == "text/html":
                            # print text/html part
                            print(body)
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print text/plain email
                        print(body)
                    if content_type == "text/html":
                        # print text/html email
                        print(body)
                print("="*100)                

def imap_test():
    email_address = 'YOUR_ACCOUNT@hotmail.com'
    password = 'YOUR_PASSWORD'
    imap_server = 'outlook.office365.com'
    imap_port = 993
    socks_addr = '127.0.0.1'
    socks_port = 1080
    socks_type = 'socks5'

    imap = SocksIMAP4_SSL(host=imap_server, port=imap_port, timeout=15, proxy_addr=socks_addr, proxy_port=socks_port, proxy_type=socks_type)
    imap.login(email_address, password)
    print_inbox(imap)
    imap.logout()

imap_test()
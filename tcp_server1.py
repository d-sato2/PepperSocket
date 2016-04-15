from __future__ import print_function
import socket
from contextlib import closing
import datetime

def main():
  host = '192.168.1.179'
  port = 4000
  backlog = 10
  bufsize = 4096
  now = datetime.datetime.now()
  mili = now.strftime("%Y%m%d%H%M%S.") + "%04d" % (now.microsecond // 1000)
  print (mili)

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  with closing(sock):
    sock.bind((host, port))
    sock.listen(backlog)
    while True:
      conn, address = sock.accept()
      with closing(conn):
        msg = conn.recv(bufsize)
        print(msg)
        now = datetime.datetime.now()
        mili = now.strftime("%Y%m%d%H%M%S.") + "%04d" % (now.microsecond // 1000)
        print("PCtime:" + mili)
        conn.send("PCtime:" + mili)
  return

if __name__ == '__main__':
  main()

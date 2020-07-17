from flask import Flask, request, Response
from process import parameters

app, sio = parameters()

if __name__ == "__main__":
   sio.run(app)
   print("Flask-SocketIO server launched")

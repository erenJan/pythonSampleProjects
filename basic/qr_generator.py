import pyqrcode
import png
name = input("Enter the file name : ")
text = input("Enter the message or string here : ")

qr = pyqrcode.create(text)

qr.png(str(name)+".png",scale=6)
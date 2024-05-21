import qrcode as qrc
import tkinter as tk

link = input('Copy or write link you want to generate: ') #Put link
name = input('Name of QR code: ') #user input the name of the qr code which will be the name of the file

qr = qrc.QRCode(version = 3, box_size = 15, border = 5)

## version: This parameter specifies the size of the QR code.The version number ranges from 1 to 40, with version 1 being the smallest and version 40 being the largest.In this code, the version is set to 3, which means that the QR code will be of medium size.

## box_size: This parameter specifies the size of each box or module in the QR code.In this code, the box size is set to 15 pixels.

## border: This parameter specifies the size of the border around the QR code.In this code, the border size is set to 5 modules.

qr.add_data(link)
qr.make

img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save(name +'.png')

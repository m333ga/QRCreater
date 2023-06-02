from customtkinter import *
from qrcode import make
from random import randint
from datetime import datetime

# create win
win = CTk()
win.title('QRCreater')
win.iconbitmap('Programm\icon.ico')
win.geometry('400x70')
win.resizable(width = False, height = False)

# entry
entry = CTkEntry(win,
                 width = 390,
                 border_width = 2,
                 placeholder_text = 'enter text for qr code...')
entry.grid(padx = 5, pady = 5)

qr_text = str()
def save_qrcode():
    qr_text = entry.get()

    if qr_text:
        # create qr code
        qr_image = make(qr_text,
                        box_size = 15,
                        border = 1)

        qr_image.save(f'QR Codes\QRCode_{qr_text[:15]}.jpg') # save as image

        win.quit()


# save button
save_button = CTkButton(win,
                        text = 'Create QR',
                        width = 70, height = 25,
                        border_width = 1,
                        text_color = '#ffffff', text_color_disabled = '#c4c4c4',
                        fg_color = '#696969', hover_color = '#363636',
                        command = save_qrcode)
save_button.grid(pady = 0)

# end
win.mainloop()
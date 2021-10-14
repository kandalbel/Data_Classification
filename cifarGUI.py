
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,  Image
import numpy

from keras.models import load_model

model = load_model('cifar_model_Saved.h5')

classes = {
    0: 'Uçak',
    1: 'Araba',
    2: 'Kuş',
    3: 'Kedi',
    4: 'Geyik',
    5: 'Köpek',
    6: 'Kurbağa',
    7: 'At',
    8: 'Gemi',
    9: 'Kamyon'
}

#resim yukleme
def upload_image():
    file_path = filedialog.askopenfilename()
    uploaded = Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
    im = ImageTk.PhotoImage(uploaded)
    sign_image.configure(image=im)
    sign_image.image = im
    label.configure(text='' )
    show_classify_button(file_path)

#siniflandirma buton
def show_classify_button(file_path):
    classify_btn = Button(top, text ="Görüntüyü sınıflandır", command=lambda: classify(file_path),padx=10, pady=5)
    classify_btn.configure(background = "#364156", foreground = "white",font= ('arial', 10, 'bold'))
    classify_btn.place(relx=0.79,rely=0.46)

#siniflandirma
def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((32,32))
    image = numpy.expand_dims(image, axis =0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)
    label.configure(foreground= '#011638', text = sign)

#GUI oluşturma
top = tk.Tk()
top.geometry('800x600')
top.title("CIFAR10 veri kümesi görüntü Sınıflandırma")
top.configure(background = "#CDCDCD")

#başlık
heading = Label(top, text = "CIFAR10 veri kümesi görüntü Sınıflandırma", pady=20, font=('arial', 20, 'bold'))
heading.configure(background = "#CDCDCD", foreground = '#364156')
heading.pack()

upload = Button(top, text= "fotoğraf yükle", command=upload_image, padx=10, pady=5)
upload.configure(background = "#364156", foreground='white', font = ('arial',10,'bold'))
upload.pack(side = BOTTOM, pady=50)

#Fotoğraf yükleme
sign_image = Label(top)
sign_image.pack(side = BOTTOM, expand = True)

label = Label(top, background = "#CDCDCD", font = ('arial', 15, 'bold'))
label.pack(side= BOTTOM, expand = True)

top.mainloop()

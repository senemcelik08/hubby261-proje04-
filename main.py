import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Label
from tkinter import Button
import PyPDF2 # PDF dosyaları için
from docx import Document # Word dosyaları için
from wordcloud import WordCloud # Kelime bulutu oluşturmak için
import matplotlib.pyplot as plt # Bulutu görüntülemek için
import nltk

# NLTK kütüphanesi kullanarak ingilizce ve Türkçe stop wordleri çıkarabilirsiniz

import nltk
from nltk.corpus import stopwords

# İngilizce stop wordleri
stop_words_en = set(stopwords.words("english"))
# Türkçe stop wordleri
stop_words_tr = set(stopwords.words("turkish"))

# Dosya yolunu ve dosya adını değişkenlere atayın
file_path = ""
file_name = ""

def upload_file():
    global file_path
    global file_name
    file_path = filedialog.askopenfilename()
    file_name = file_path.split("/")[-1]

def create_wordcloud():
    global file_path
    global file_name
    if file_path == "":
        messagebox.showerror("Error", "Lütfen bir dosya seçiniz.")
    else:
        # Dosya türüne göre okuma işlemi
        if file_name.endswith('.pdf'):
            pdfFileObj = open(file_path,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            text = ""
            for page in range(pdfReader.numPages):
                text += pdfReader.getPage(page).extractText()
        elif file_name.endswith('.docx'):
            doc = Document(file_path)
            text = ""
            for para in doc.paragraphs:
                text += para.text

        # Stop wordleri çıkarın
        filtered_text = [word for word in text.split() if word.lower() not in stop_words_en and word.lower() not in stop_words_tr]

        # Kelime bulutunu oluşturun
        wordcloud = WordCloud().generate(" ".join(filtered_text))

        # Bulutu görüntüleyin
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

root = tk.Tk()


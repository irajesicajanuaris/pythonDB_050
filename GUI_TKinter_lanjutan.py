import tkinter as tk
from tkinter import ttk
import sqlite3


uiApp = tk.Tk()
uiApp.configure(background='grey')
uiApp.geometry("800x1000")
uiApp.resizable()
uiApp.title("Prediksi Prodi Pilihan")

#make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=50,fill="x", expand=True)  

#make label
inputLabel = ttk.Label(inputFrame, text="Prediksi Prodi Pilihan")
inputLabel.pack(padx=10, pady=10, fill="x", expand=True)

#input nama siswa
labelInputNama = ttk.Label(inputFrame, text="Masukkan Nama Siswa")
labelInputNama.pack(padx=10, pady=5, fill="x", expand=True)

entryInputNama = ttk.Entry(inputFrame)
entryInputNama.pack(padx=10, pady=5, fill="x", expand=True)

#input nilai 
labelInputBiologi = ttk.Label(inputFrame, text="Masukkan nilai Biologi kamu")
labelInputBiologi.pack(padx=10, pady=5, fill="x", expand=True)

entryInputBiologi = ttk.Entry(inputFrame)
entryInputBiologi.pack(padx=10, pady=5, fill="x", expand=True)


labelInputFisika = ttk.Label(inputFrame, text="Masukkan nilai fisika kamu")
labelInputFisika.pack(padx=10, pady=5, fill="x", expand=True)

entryInputFisika = ttk.Entry(inputFrame)
entryInputFisika.pack(padx=10, pady=5, fill="x", expand=True)


labelInputInggris = ttk.Label(inputFrame, text="Masukkan nilai bahasa inggris kamu")
labelInputInggris.pack(padx=10, pady=5, fill="x", expand=True)

entryInputInggris = ttk.Entry(inputFrame)
entryInputInggris.pack(padx=10, pady=5, fill="x", expand=True)

def dataEntry():
    nama_siswa = entryInputNama.get()
    nilai_Biologi = float(entryInputBiologi.get())
    nilai_Fisika = float(entryInputFisika.get())
    nilai_Inggris = float(entryInputInggris.get())

    prediksi = ""

    if nilai_Biologi > nilai_Fisika and nilai_Fisika > nilai_Inggris:
        prediksi = "Kedokteran"
    elif nilai_Fisika > nilai_Biologi and nilai_Fisika > nilai_Inggris:
        prediksi = "Teknik"
    elif nilai_Inggris > nilai_Biologi and nilai_Inggris > nilai_Fisika:
        prediksi = "Bahasa"
    else:
        return "Tidak Dapat Diprediksi"
    
    label_hasil.config(text=f"Hasil Prediksi untuk {nama_siswa} adalah {prediksi}")
    
    # Simpan data ke database SQLite
    conn = sqlite3.connect('iradb.db')
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        prediksi_fakultas TEXT
                    )''')

    # Menyimpan nilai siswa ke dalam database
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
                      VALUES (?, ?, ?, ?, ?)''', (nama_siswa, nilai_Biologi, nilai_Fisika, nilai_Inggris, prediksi))
    
    conn.commit()
    conn.close()

buttonSubmit = ttk.Button(inputFrame, text="Hasil Prediksi", command=dataEntry)
buttonSubmit.pack(padx=10, pady=10, fill="x", expand=True)

label_hasil = tk.Label(inputFrame, text="")
label_hasil.pack()

uiApp.mainloop()
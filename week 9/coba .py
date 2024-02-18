import tkinter as tk

def hitung_diskon():
    total_belanja = float(entry_total.get())

    if total_belanja >= 1000000:
        diskon = 0.15 * total_belanja
    elif total_belanja >= 500000:
        diskon = 0.1 * total_belanja
    elif total_belanja >= 200000:
        diskon = 0.05 * total_belanja
    else:
        diskon = 0

    total_setelah_diskon = total_belanja - diskon
    label_hasil['text'] = f"Total belanja setelah diskon: Rp {total_setelah_diskon:,.2f}"

# Membuat jendela utama
root = tk.Tk()
root.title('Aplikasi Hitung Diskon')

# Membuat label dan entry untuk input total belanja
label_total = tk.Label(root, text='Masukkan total belanja:')
label_total.pack()

entry_total = tk.Entry(root)
entry_total.pack()

# Tombol untuk menghitung diskon
button_hitung = tk.Button(root, text='Hitung Diskon', command=hitung_diskon)
button_hitung.pack()

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text='')
label_hasil.pack()

root.mainloop()

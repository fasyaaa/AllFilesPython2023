import tkinter as tk

def konversi_suhu():
    try:
        nilai_suhu = float(entry_suhu.get())

        if var_mode.get() == 1:  # Jika mode Celcius dipilih
            fahrenheit = (nilai_suhu * 9/5) + 32
            kelvin = nilai_suhu + 273.15
            label_hasil['text'] = f"Fahrenheit: {fahrenheit:.2f} F\nKelvin: {kelvin:.2f} K"
        elif var_mode.get() == 2:  # Jika mode Fahrenheit dipilih
            celcius = (nilai_suhu - 32) * 5/9
            kelvin = (nilai_suhu + 459.67) * 5/9
            label_hasil['text'] = f"Celcius: {celcius:.2f} C\nKelvin: {kelvin:.2f} K"
        elif var_mode.get() == 3:  # Jika mode Kelvin dipilih
            celcius = nilai_suhu - 273.15
            fahrenheit = (nilai_suhu * 9/5) - 459.67
            label_hasil['text'] = f"Celcius: {celcius:.2f} C\nFahrenheit: {fahrenheit:.2f} F"
        else:
            label_hasil['text'] = "Pilih mode konversi suhu!"
    except ValueError:
        label_hasil['text'] = "Masukkan angka yang valid untuk suhu!"

# Membuat jendela utama
root = tk.Tk()
root.title('Konversi Suhu')

# Membuat label dan entry untuk input suhu
label_suhu = tk.Label(root, text='Masukkan suhu:')
label_suhu.pack()

entry_suhu = tk.Entry(root)
entry_suhu.pack()

# Radio button untuk memilih mode konversi suhu
var_mode = tk.IntVar()

mode_celcius = tk.Radiobutton(root, text='Celcius', variable=var_mode, value=1)
mode_celcius.pack()

mode_fahrenheit = tk.Radiobutton(root, text='Fahrenheit', variable=var_mode, value=2)
mode_fahrenheit.pack()

mode_kelvin = tk.Radiobutton(root, text='Kelvin', variable=var_mode, value=3)
mode_kelvin.pack()

# Tombol untuk melakukan konversi
button_konversi = tk.Button(root, text='Konversi', command=konversi_suhu)
button_konversi.pack()

# Label untuk menampilkan hasil konversi
label_hasil = tk.Label(root, text='')
label_hasil.pack()

root.mainloop()
# contoh pure function
def tambah(a, b):
    return a + b

# contoh penggunaan map dan filter
angka = [1, 2, 3, 4, 5]

hasil = list(map(lambda x: x * 2, angka))
# hasil = [2, 4, 6, 8, 10]

hasil_filter = list(filter(lambda x: x % 2 == 0, angka))
# hasil_filter = [2, 4]

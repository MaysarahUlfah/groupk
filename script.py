from product_item import ProductItem

# Membuat daftar komoditas dan harganya
product_item1 = ProductItem('Beras Rojolele 5 kg', 56_000)
product_item2 = ProductItem('Gulaku 1 kg', 13_000)
product_item3 = ProductItem('Terigu Mila 1 kg', 11_000)
product_item4 = ProductItem('Minyak Goreng Filma 1 ltr', 18_000)

product_items = [product_item1, product_item2, product_item3, product_item4]


print('''
Selamat datang di Koperasi Usaha Bersama
Berikut daftar harga sembako hari ini:
''')

print('--------------------')
# Menampilkan komoditas dan harganya
index = 1

for product_item in product_items:
    print(str(index) + '. ' + product_item.info())
    index += 1
print('--------------------')

# Memulai interaksi dengan user

try:
    order = int(input('Mau pesan yang mana? (masukan nomor): '))
    selected_product = product_items[order-1]
    print('Item yang di pilih: ' + selected_product.name)

# Terima input dari console, dan Berikan input ke variable count
    count = int(input('Mau berapa banyak?: '))

# Panggil method get_total_price 
    result = selected_product.get_total_price(count)

# Cetak 'Total harga adalah $____'
    print('Total harganya adalah Rp ' + str(result))
    print('Pesanan akan segera di kirim, terima kasih telah berbelanja')

except:
    print('Nomor yang Anda masukan tidak ada di daftar')

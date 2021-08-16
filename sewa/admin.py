from django.contrib import admin
from .models import *

admin.site.register(Penyewa)
admin.site.register(Barang)
admin.site.register(TempBarang)
admin.site.register(Transaksi)
admin.site.register(DetailTransaksi)
admin.site.register(Pengeluaran)
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [

    path('', views.beranda, name='beranda'),
    path('datacustomer/', views.dataCustomer, name='datacustomer'),

    path('detailtransaksi/', views.datapenyewa, name='detailtransaksi'),
    path('form_detailtransaksi/', views.form_detailtransaksi, name='form_detailtransaksi'),
    path('update_detailtransaksi/<str:pk>', views.updateDetailtransaksi, name='update_detailtransaksi'),
    path('update_kembalidetailtransaksi/<str:pk>', views.updatekembaliDetailtransaksi, name='update_kembalidetailtransaksi'),
    path('delete_detailtransaksi/<str:pk>', views.deleteDetailTransaksi, name='delete_detailtransaksi'),

    # path('transaksi/', views.datapenyewa, name='transaksi'),
    # path('form_transaksi/', views.form_transaksi, name='form_transaksi'),
    # path('update_transaksi/<str:pk>', views.updatetransaksi, name='update_transaksi'),
    # path('update_kembalitransaksi/<str:pk>', views.updatekembalitransaksi, name='update_kembalitransaksi'),
    # path('delete_transaksi/<str:pk>', views.deleteTransaksi, name='delete_transaksi'),

    path('formproduct/', views.formproduct, name='formproduct'),
    path('form_product/', views.form_product, name='form_product'),
    path('update_product/<str:pk>', views.updateProduct, name='update_product'),
    path('delete_product/<str:pk>', views.deleteProduct, name='delete_product'),
    
    path('register/', views.Register, name='register'),
    path('login-page/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('laporandatapenyewa/', views.laporandatapenyewa, name='laporandatapenyewa'),
    path('export-exceldp/', views.exportdatapenyewa, name='export-exceldp'),
    path('laporanpembayaran/', views.laporanpembayaran, name='laporanpembayaran'),
    path('export-pembayaran/', views.exportpembayaran, name='export-pembayaran'),
    path('pengeluaran/', views.pengeluaran, name='pengeluaran'),
    path('form-pengeluaran/', views.form_pengeluaran, name='form_pengeluaran'),
    path('update_pengeluaran/<str:pk>', views.updatePengeluaran, name='update_pengeluaran'),
    path('delete_pengeluaran/<str:pk>', views.deletePengeluaran, name='delete_pengeluaran'),
    # path('export/', views.export, name='export'),
    path('export-excel/', views.export, name='export-excel'),

    path('userpage/', views.userPage, name='userpage'),

    ###### ecommerce_tutorial_youtube#######

    path('berandapenyewa1', views.page_barang, name='berandapenyewa1'),
    path('tampilbarangjs', views.tampilbarangjs, name='tampilbarangjs'),
    path('tampilkeranjangjs', views.tampilkeranjangjs, name='tampilkeranjangjs'),
    path('simpankeranjang/', views.simpankeranjang, name='simpankeranjang'),
    path('keranjanghapus/', views.keranjanghapus, name='keranjanghapus'),
    path('simpantransaksi/', views.simpantransaksi, name='simpantransaksi'),

    path('account/', views.accountSetting, name='account-page'),

]
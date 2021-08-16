from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
import uuid
# import csv
import xlwt
import datetime
# from io import BytesIO
# from xhtml2pdf import pisa
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.models import Group
from django.views.generic import View

# Create your views here.
from .models import *
from .forms import PenyewaForm, FormPengeluaran, FormBarang, TempBarangForm, TransaksiForm, DetailTransaksiFormbayar, DetailTransaksiFormkembali
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
from django.db.models import Sum

@login_required(login_url='login')
@pilihan_login
def beranda(request):
    total_barang = Barang.objects.count()
    total_penyewa = Penyewa.objects.count()
    total_detailtransaksi = DetailTransaksi.objects.count()
    total_pengeluaran = Pengeluaran.objects.count()
    context ={
        "menu" : 'beranda',
        "page" : 'Selamat Datang di penyewaan aset BUMDes',
        "data_total_barang": total_barang,
        "data_total_penyewa": total_penyewa,
        "data_total_detailtransaksi": total_detailtransaksi,
        "data_total_pengeluaran": total_pengeluaran,
    }
    return render(request, 'sewa/beranda.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def dataCustomer(request):
    list_penyewa = Penyewa.objects.all()
    context = {
        'judul': 'Halaman Penyewa',
        'menu': 'penyewa',
        'list_penyewa': list_penyewa,
    }
    return render(request, 'sewa/datacustomer.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def datapenyewa(request):
    list_detailtransaksi = DetailTransaksi.objects.all()
    context = {
        'judul': 'Halaman Data Penyewa',
        'menu': 'datapenyewa',
        'list_detailtransaksi': list_detailtransaksi,
    }
    return render(request, 'sewa/detailtransaksi.html', context)

@login_required(login_url='login')
@pilihan_login
def form_detailtransaksi(request):
    form_detailtransaksi = DetailTransaksiForm()
    if request.method == 'POST':
        formsimpan = DetailTransaksiForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('formdetailtransaksi')
    context = {
        'judul': 'Form Detailtransaksi',
        'menu' : 'DetailTransaksi', 
        'form': form_detailtransaksi

    }
    return render(request, 'sewa/form_detailtransaksi.html', context)

@login_required(login_url='login')
@pilihan_login
def updateDetailtransaksi(request, pk):
    detailtransaksi = DetailTransaksi.objects.get(id=pk)
    form_detailtransaksi = DetailTransaksiFormbayar(instance=detailtransaksi) 
    if request.method == 'POST':
        print('Cetak POST:', request.POST)
        formedit = DetailTransaksiFormbayar(request.POST, instance=detailtransaksi)
        if formedit.is_valid:
            formedit.save()
            return redirect('/detailtransaksi')
    context = {
        'judul': 'Edit Form DetailTransaksi',
        'form' : form_detailtransaksi,
    }
    return render(request, 'sewa/form_detailtransaksi.html', context)
    
def updatekembaliDetailtransaksi(request, pk):
    detailtransaksi = DetailTransaksi.objects.get(id=pk)
    form_detailtransaksi = DetailTransaksiFormkembali(instance=detailtransaksi)
    if request.method == 'POST':
        idbrg = detailtransaksi.barang.id
        stokdetail = detailtransaksi.barang.stok
        tranjumlah = detailtransaksi.jumlah
        updatebrg = Barang.objects.get(id=idbrg)
        updatebrg.stok = stokdetail + tranjumlah
        updatebrg.save()
        formedit = DetailTransaksiFormkembali(request.POST, instance=detailtransaksi)
        if formedit.is_valid:
            formedit.save()
            return redirect('/detailtransaksi')
    context = {
        'judul': 'Edit Form DetailTransaksi',
        'form' : form_detailtransaksi,
    }
    return render(request, 'sewa/form_detailtransaksi.html', context)

@login_required(login_url='login')
@pilihan_login
def deleteDetailTransaksi(request, pk):
    detailtransaksihapus = DetailTransaksi.objects.get(id=pk)
    if request.method == 'POST':
        detailtransaksihapus.delete()
        return redirect('/detailtransaksi')
    context = {
        'judul': 'Hapus  Detailtransaksi',
        'detailtransaksidelete' :  detailtransaksihapus,
    }
    return render(request, 'sewa/delete_detailtransaksi.html', context)

@tolakhalaman_ini
def loginPage (request):
    formlogin = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        cocokan = authenticate(request, username=username, password=password )
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda')
    context = {
        'judul': 'Halaman Login',
        'menu': 'login',
        'tampillogin' : formlogin
    }
    return render(request, 'sewa/login.html', context)

@tolakhalaman_ini
def Register(request): 
    form = PenyewaForm()
    formpenyewa = PenyewaForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username = username).first():
            messages.success(request, 'Username sudah ada.')
            return redirect('login')

        if password1 != password2:
            messages.success(request, 'Password Tidak sama')
            return redirect('login')

        # user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()
        # user

        # Group
        sewa_penyewa = Group.objects.get(name='penyewa')
        user.groups.add(sewa_penyewa)
        # Group

        # Karyawan
        formsimpanpenyewa = formpenyewa.save()
        formsimpanpenyewa.user = user
        formsimpanpenyewa.save()  

        return redirect('login')

    context = {
        'menu' : 'Form Penyewa',
        'page' : 'form penyewa',  
        'form' : form,      
    }
    return render(request, 'sewa/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@pilihan_login
def laporandatapenyewa(request):
    list_detailtransaksi = DetailTransaksi.objects.filter(keterangan='Bayar')
    context = {
        'judul': 'Halaman Laporan Data Penyewa',
        'menu': 'laporan datapenyewa',
        'list_detailtransaksi': list_detailtransaksi,
    }
    return render(request, 'sewa/laporandatapenyewa.html', context)

def exportdatapenyewa(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Data Penyewa' + \
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Penyewa')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nik', 'Nama', 'Alamat']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    
    rows = Penyewa.objects.filter().values_list('nik', 'name', 'alamat')
    
    for row in rows:
        row_num += 1

        print('row_num', row_num)

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response


@login_required(login_url='login')
@pilihan_login
def laporanpembayaran(request):
    list_detailtransaksi = DetailTransaksi.objects.filter(keterangan='Bayar')
    context = {
        'judul': 'Halaman Laporan Pembayaran',
        'menu': 'laporan pembayaran',
        'list_detailtransaksi': list_detailtransaksi,
    }
    return render(request, 'sewa/laporanpembayaran.html', context)

def exportpembayaran(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Data Pembayaran' + \
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('DetailTransaksi')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['NIK','NAMA', 'PRODUCT', 'BAYAR']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    
    rows = DetailTransaksi.objects.filter().values_list('penyewa__nik', 'penyewa__name', 'barang__barang', 'barang__harga')   
    
    for row in rows:
        row_num += 1

        # print('row_num', row_num)

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response

@login_required(login_url='login')
@pilihan_login
def pengeluaran(request):
    form_pengeluaran = FormPengeluaran.objects.all()
    context={
        'judul': 'Halaman Pengeluaran',
        'menu': 'pengeluaran'      
    }
    return render(request, 'sewa/pengeluaran.html', context)

@login_required(login_url='login')
@pilihan_login
def form_pengeluaran(request):
    form_pengeluaran = FormPengeluaran()
    if request.method == 'POST':
        formsimpan = FormPengeluaran(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pengeluaran')
    context = {
        'judul': 'Form Pengeluaran',
        'menu' : 'Pengeluaran', 
        'form': form_pengeluaran
    }
    return render(request, 'sewa/form_pengeluaran.html', context)

@login_required(login_url='login')
@pilihan_login
def pengeluaran(request):
    list_pengeluaran = Pengeluaran.objects.all()
    
    # total_price = DetailTransaksi.objects.filter(keterangan='Bayar').aggregate(Sum('barang__harga'))

    total_bayar = DetailTransaksi.objects.all().filter(keterangan='Bayar')
    sum = 0
    for item in total_bayar :
        sum = sum + item.hargatotal


    total_keluar = Pengeluaran.objects.all().aggregate(Sum('biaya'))
    saldo = sum - total_keluar['biaya__sum']
    context = {
        'judul': 'Halaman Pengeluaran',
        'menu': 'pengeluaran',   
        'list_pengeluaran': list_pengeluaran,
        'total' : sum,
        'saldo': saldo
    }
    return render(request, 'sewa/pengeluaran.html', context)

def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Data Pengeluaran' + \
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pengeluaran')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Tanggal_pengeluaran', 'Keterangan', 'Biaya']

    
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    
    rows = Pengeluaran.objects.filter().values_list('tanggal_pengeluaran', 'keterangan', 'biaya')
    
    for row in rows:
        row_num += 1

        # print('row_num', row_num)

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response

@login_required(login_url='login')
@pilihan_login
def updatePengeluaran(request, pk):
    pengeluaran = Pengeluaran.objects.get(id=pk)
    form_pengeluaran = FormPengeluaran(instance=pengeluaran)
    if request.method == 'POST':
        formedit = FormPengeluaran(request.POST, instance=pengeluaran)
        if formedit.is_valid:
            formedit.save()
            return redirect('/pengeluaran')
    context = {
        'judul': 'Edit Pengeluaran',
        'form' : form_pengeluaran,
    }
    return render(request, 'sewa/form_pengeluaran.html', context)

@login_required(login_url='login')
@pilihan_login
def deletePengeluaran(request, pk):
    pengeluaranhapus = Pengeluaran.objects.get(id=pk)
    if request.method == 'POST':
        pengeluaranhapus.delete()
        return redirect('/pengeluaran')
    context = {
        'judul': 'Hapus Pengeluaran',
        'pengeluarandelete' : pengeluaranhapus,
    }
    return render(request, 'sewa/delete_pengeluaran.html', context)

def userPage(request):
    detailtransaksi_penyewa = request.user.penyewa.detailtransaksi_set.all()
    context = {
        'data_detailtransaksi_penyewa':detailtransaksi_penyewa,
    }
    return render(request, 'sewa/user.html', context)

def accountSetting(request):
    datapenyewa = request.user.penyewa
    form = PenyewaForm(instance = datapenyewa)
    if request.method == 'POST':
        form = PenyewaForm(request.POST, request.FILES, instance=datapenyewa)
        if form.is_valid:
            form.save() 
    context = {
        'menu': 'settings',
        'formpenyewa': form 
    }
    return render(request, 'sewa/account_setting.html', context)

########DATABARANG/ASET#######

@login_required(login_url='login')
@pilihan_login
def formproduct(request):
    formbarang = Barang.objects.all()
    penyewa = request.user.penyewa
    context ={
        "menu" : 'Form Barang',
        "page" : 'Form Barang',
        'product' : formbarang
    }
    return render(request, 'sewa/formproduct.html', context)

@login_required(login_url='login')
@pilihan_login
# tambah barang
def form_product(request):
    form_barang = FormBarang()
    if request.method == 'POST':
        formsimpan = FormBarang(request.POST, request.FILES)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('formproduct')
    context = {
        'judul': 'Form Barang',
        'menu' : 'Barang',
        'form': form_barang

    }
    return render(request, 'sewa/form_product.html', context)

@login_required(login_url='login')
@pilihan_login
# update barang
def updateProduct(request, pk):
    formproduct = Barang.objects.get(id=pk)
    form_product = FormBarang(instance=formproduct)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = FormBarang(request.POST, request.FILES, instance=formproduct)
        if formedit.is_valid:
            formedit.save()
            return redirect('/formproduct')
    context = {
        'judul': 'Edit Form Barang',
        'form' : form_product,
    }
    return render(request, 'sewa/form_product.html', context)

@login_required(login_url='login')
@pilihan_login
def formproduct(request):
    list_barang = Barang.objects.all()
    context = {
        'judul': 'Halaman Barang',
        'menu': 'barang',
        'list_barang': list_barang,
    }
    return render(request, 'sewa/formproduct.html', context)

@login_required(login_url='login')
@pilihan_login
def deleteProduct(request, pk):
    formproducthapus = Barang.objects.get(id=pk)
    if request.method == 'POST':
        formproducthapus.delete()
        return redirect('/formproduct')
    context = {
        'judul': 'Hapus Barang',
        'formproductdelete' : formproducthapus,
    }
    return render(request, 'sewa/delete_product.html', context)

#########ECOMERCE_TUTORIAL_YOUTUBE#######
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['penyewa'])
def page_barang(request):
    no = Transaksi.objects.all().count()
    
    notransaksi =1000 + int(no)
    context = {
        'judul': 'Halaman Beranda Penyewa',
        'notransaksi':notransaksi
    }
    return render(request, 'sewa/berandapenyewa.html', context)

def simpantransaksi(request):
    if request.method == 'POST':
        no_transaksi = str(uuid.uuid4())
        grantotal = request.POST.get('grantotal')
        penyewa = request.user.penyewa
        transaksi = Transaksi.objects.create(no_transaksi = no_transaksi ,penyewa = penyewa, total_transaksi = grantotal )
        transaksi.save()

        temp = TempBarang.objects.order_by('-id').filter(penyewa=request.user.penyewa)
        for r in temp:
            instance_detail= DetailTransaksi(
                no_transaksi = no_transaksi,
                # total_transaksi = grantotal,
                penyewa = request.user.penyewa,
                barang = r.barang,
                jumlah = r.jumlah,
                keterangan="Belum Bayar",
                status=r.status,
                pengembalian="Belum Kembali",
                tanggal_kembali= r.tanggal_kembali,
                jml_pinjam= r.jml_pinjam
            )
            instance_detail.save()
        temp.delete()
        return JsonResponse({'status': 0 })
    else:
        return JsonResponse({'status': 0 })

# Mesin JS

def tampilbarangjs(request):
    barang = Barang.objects.order_by('-id')
    context = {
        'brg' : barang,
    }
    return render(request, 'sewa/js/barang.html', context)

def tampilkeranjangjs(request):
    temp = TempBarang.objects.order_by('-id').filter(penyewa=request.user.penyewa)
    hitungtemp= temp.count()
    total_all =0
    for r in temp:
        grand = r.hargatotal
        total_all += grand
    context = {
        "temp" : temp,
        "sum": total_all,
        'hitungtemp': hitungtemp
    }
    return render(request, 'sewa/js/keranjang.html', context)

def simpankeranjang(request):
    if request.method == "POST":
        id = request.POST.get('id')
        sts = request.POST['status']
        jumlah_pinjam = request.POST['jumlah_pinjam']
        penyewa = request.user.penyewa
        idbarang = Barang.objects.get(pk=id)

        cek_temp = TempBarang.objects.filter(penyewa=penyewa, barang=idbarang).count()
        if cek_temp > 0:
            temp =TempBarang.objects.get(penyewa=penyewa, barang=idbarang)
            temp.jumlah+=1
            temp.save()

            idbarang.stok-=1
            idbarang.save()
            return JsonResponse({'status': 'Save' })
        else:
            idbarang.stok-=1
            idbarang.save()

            temp = TempBarang.objects.create(penyewa=penyewa, barang = idbarang, jumlah = 1, status = sts, jml_pinjam = jumlah_pinjam )
            temp.save()
            return JsonResponse({'status': 'Save' })
    else:
        return JsonResponse({'status': 0 })

def keranjanghapus(request):
    if request.method == "POST":
        id = request.POST.get('id')
        idbrg = request.POST.get('idbrg')
        jml = request.POST['jml']

        temp = TempBarang.objects.get(pk=id)
        temp.delete()

        idbarang = Barang.objects.get(pk=idbrg)
       
        idbarang.stok+=int(jml)
        idbarang.save()

        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
# Mesin JS
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime

# Create your models here.

class Penyewa(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nik =  models.CharField(max_length=200, blank=True, null=True) 
    name = models.CharField(max_length=200, blank=True, null=True) 
    alamat =  models.CharField(max_length=200, blank=True, null=True)
    telepon =  models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length= 200, null=True)
    
    def __str__(self): 
        # return self.nik 
        return '%s, %s' % (self.name, self.nik)
    class Meta:
        verbose_name_plural ="Penyewa"
        
class Barang(models.Model): 
    Status=(
        ('harian', 'harian'),
        ('tahunan', 'tahunan'),
    )
    barang = models.CharField(max_length=200, blank=True, null=True)
    harga = models.BigIntegerField(blank=True, null=True)
    stok = models.IntegerField(blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=Status)
    image = models.ImageField(default='fotokosong.gif', blank=True)
    
    def __str__(self):
        return self.barang 
    class Meta:
        verbose_name_plural ="Barang"

    def save(self, *args, **kwargs):
        super(Barang, self).save(*args, **kwargs)
            
        img = Image.open(self.image.path)
            
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
    @property
    def imageURL(self):
            try:
                url = self.image.url
            except:
                url =''
            return url

class TempBarang(models.Model):
    tahun = 365
    Status=(
        ('Harian', 'Harian'),
        ('Tahunan', 'Tahunan'),
    )
    penyewa =  models.ForeignKey(Penyewa, null=True, on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, null= True, on_delete=models.SET_NULL)
    # total_transaksi = models.BigIntegerField(blank=True, null=True)
    jumlah = models.IntegerField(blank=True, null=True)
    jml_pinjam = models.IntegerField(blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=Status)
    tanggal_kembali = models.DateTimeField(auto_now_add=False, null=True)

    @property
    def hargatotal(self):
        total = self.barang.harga * self.jumlah * self.jml_pinjam
        return total

    def __str__(self):
        return f"{self.penyewa}-{self.barang}-{self.jumlah}" 
    class Meta:
        verbose_name_plural ="TempBarang"

    def save(self, *args, **kwargs):
        if self.status == "tahunan":
            if self.tanggal_kembali is None:
                self.tanggal_kembali = datetime.date.today() + datetime.timedelta(days=int(self.jml_pinjam)*self.tahun)
            super(TempBarang, self).save(*args, **kwargs)
            
        else:
            if self.tanggal_kembali is None:
                self.tanggal_kembali = datetime.date.today() + datetime.timedelta(days=int(self.jml_pinjam))
            super(TempBarang, self).save(*args, **kwargs)

class Transaksi(models.Model):  
    no_transaksi = models.CharField(max_length=200, blank=True, null=True)
    penyewa =  models.ForeignKey(Penyewa, null=True, on_delete=models.CASCADE)
    total_transaksi = models.BigIntegerField(blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
         return f"{self.no_transaksi}-{self.penyewa}({self.total_transaksi})" 
    class Meta:
        verbose_name_plural ="Transaksi"

class DetailTransaksi(models.Model):
    keterangan=(
        ('Bayar', 'Bayar'),
        ('Belum Bayar', 'Belum Bayar'),
    )
    Status=(
        ('Harian', 'Harian'),
        ('Tahunan', 'Tahunan'),
    )
    Pengembalian=(
        ('Kembali', 'Kembali'),
        ('Belum Kembali', 'Belum Kembali'),
    )
    
    no_transaksi = models.CharField(max_length=200, blank=True, null=True)
    penyewa =  models.ForeignKey(Penyewa, null=True, on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, null= True, on_delete=models.SET_NULL)
    jumlah = models.IntegerField(blank=True, null=True)
    jml_pinjam = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=Status)
    keterangan = models.CharField(max_length=200, null=True, choices=keterangan)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    tanggal_kembali = models.DateTimeField(max_length=200, blank=True, null=True)
    pengembalian = models.CharField(max_length=200, blank=True, null=True, choices=Pengembalian)

    @property
    def hargatotal(self):
        total = self.barang.harga * self.jumlah * self.jml_pinjam
        return total

    def __str__(self):
        return f"No Transaksi: {self.no_transaksi} Barang: {self.barang} Penyewa: {self.penyewa} Jumlah: {self.jumlah}" 

    class Meta:
        verbose_name_plural ="DetailTransaksi"

class Pengeluaran(models.Model):
    tanggal_pengeluaran= models.DateTimeField(auto_now_add=True, null=True)
    keterangan = models.CharField(max_length=200, blank=True, null=True)
    biaya = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.keterangan 
        
    class Meta:
        verbose_name_plural ="Pengeluaran"
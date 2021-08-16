from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pengeluaran, Barang, Penyewa, TempBarang, Transaksi, DetailTransaksi

class PenyewaForm(ModelForm):
    class Meta:
        model = Penyewa
        fields= ['nik', 'name', 'alamat', 'telepon', 'email']

        widgets = {
            'nik': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'nik': forms.TextInput(attrs={'class': 'form-control'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
     
class FormPenyewa(ModelForm):
    class Meta:
        model = Penyewa
        fields= '__all__'

class TransaksiForm(ModelForm):
    class Meta:
        model = Transaksi
        fields= '__all__'

class DetailTransaksiFormbayar(ModelForm):
    class Meta:
        model = DetailTransaksi
        fields= ['keterangan']

        widgets = {
                'keterangan': forms.Select(attrs={'class': 'form-select'})
               
            }

class DetailTransaksiFormkembali(ModelForm):
    class Meta:
        model = DetailTransaksi
        fields= ['pengembalian']

        widgets = {
                'pengembalian': forms.Select(attrs={'class': 'form-select'})
               
            }

class BarangForm(ModelForm):
    class Meta:
        model = Barang
        fields= '__all__'

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields= '__all__'

class PengeluaranForm(ModelForm):
    class Meta:
        model = Pengeluaran
        fields= '__all__'

class FormPengeluaran(ModelForm):
    class Meta:
        model = Pengeluaran
        fields= '__all__'

class Penyewa(forms.ModelForm):
    class Meta:
        model = Pengeluaran
        fields= '__all__'

class TempBarangForm(ModelForm):
    class Meta:
        model = TempBarang
        fields= '__all__'
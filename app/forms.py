from django import forms 
from .models import Product,Supplier,Category

class login_form(forms.Form):
    username = forms.CharField(
        max_length=122,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

class reg_form(forms.Form):

    Username = forms.CharField( max_length=122, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    Email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class productForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = '__all__'


class supplierForm (forms.ModelForm):
    class Meta :
        model = Supplier
        fields = '__all__'
        
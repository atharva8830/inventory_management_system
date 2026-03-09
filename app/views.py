from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from .forms import login_form , reg_form , productForm, supplierForm, transForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Product , Category , Supplier , InventoryTransaction
from django.db.models import Count


def base_view(request):
    return render (request , 'landing.html')


@login_required
def home_view(request):
    return render (request , 'home.html')


def login_view(request):
    
    flag = 0 

    if request.method == 'POST':
        name = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = name , password = password)

        if user is not None:
            login(request , user)
            print (name , password)
            return redirect('home')
        else :
            flag = 1
            # return HttpResponse("<h1>wrong crediantials</h1>")


    form = login_form()
    return render (request , 'login.html' , {'form' : form , 'flag' : flag })


def register_view(request):
    form = reg_form()
    if request.method == 'POST':
        name = request.POST['Username']
        passo = request.POST['password']
        print(name , passo)
        User.objects.create_user(username = name , password = passo)
        return redirect('login')
    return render (request , 'reg.html' , {'form' : form})



def landing_view(request):
    return render(request , 'landing.html') 


def logout_view(request):
    
    logout(request)
    return redirect('landing')



def prod_view(request):

    item = Product.objects.all()
    
    return render (request , 'products.html' , {'item' : item})


def add_view (request):
    form = productForm()
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prod')
    return render (request , 'add.html' , {'form' : form })


def delete_view(request , id ):
    product = get_object_or_404(Product , id=id)
    product.delete()
    return redirect('prod')


def update_view(request , id):

    product = get_object_or_404(Product , id = id )
    if request.method == 'POST':
            form = productForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('prod')
    form = productForm(instance= product )
    return render (request , 'update.html', {'form' : form})



def supplier_view(request):
    data = Supplier.objects.all()
    return render (request , 'supplier.html' , {'data' : data})

def add_supplier (request):

    if request.method == 'POST':
        form = supplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sup')
    form = supplierForm()
    return render(request , 'add_supplier.html' , {'form' : form})

def del_supplier(request , id):
    product = get_object_or_404(Supplier , id=id)
    product.delete()
    return redirect('sup')

def update_supplier(request , id):
    supp = get_object_or_404(Supplier , id = id )

    if request.method == 'POST':
        form = supplierForm(request.POST , instance = supp)
        form.save()
        return redirect('sup')

    form = supplierForm(instance = supp)
    return render (request , 'update_supplier.html' , {'form' : form})


def inventory_transactions(request):

    transactions = InventoryTransaction.objects.all().order_by('-created_at')

    return render(request, 'inventory_transactions.html', {'transactions': transactions})


def invForm (request):
    form = transForm()

    if request.method == 'POST':
        form = transForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trans')

    return render (request , 'invenForm.html' , {'form' : form})


def dashboard(request):

    # Stock movement
    stock_in = InventoryTransaction.objects.filter(
        transaction_type='IN'
    ).count()

    stock_out = InventoryTransaction.objects.filter(
        transaction_type='OUT'
    ).count()

    # Category chart
    category_data = Product.objects.values('category__name').annotate(
        total=Count('id')
    )

    labels = [item['category__name'] for item in category_data]
    data = [item['total'] for item in category_data]

    # Low stock products
    low_products = Product.objects.filter(quantity__lt=10)

    low_labels = [p.name for p in low_products]
    low_data = [p.quantity for p in low_products]

    context = {
        'stock_in': stock_in,
        'stock_out': stock_out,
        'labels': labels,
        'data': data,
        'low_labels': low_labels,
        'low_data': low_data
    }

    return render(request, 'dashboard.html', context)
from django.shortcuts import render, redirect
from .models import details_table, register_table
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password



# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        email = request.POST['email']
        print(email)
        country = request.POST['country']
        print(country)
        password = request.POST['password']
        print(password)

        if register_table.objects.filter(username=username).exists():
            messages.error(request,"Username already exist.")
            return redirect('register')
        
        registers = register_table(username=username, email=email, country=country, password=password)
        registers.save()
        messages.success(request, 'Registration successful Please log in.')
        return redirect("login")
    
    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["password"]

        # if register_table.objects.filter(username=username, password=password):
        #     return redirect("index.html") 
        # messages.MessageFailure("Username or Password is incorrect")

        # try:
        #     user = register_table.objects.get(username=username)

        #     if check_password(password, user.password):
        #         request.session['user_id'] = user.id
        #         return redirect('')
    return render(request, "register.html")


def table(request):
    return render(request, "table.html")

def buttons(request):
    return render(request, "buttons.html")

def dropdowns(request):
    return render(request, "dropdowns.html")

def typography(request):
    return render(request, "typography.html")

def basic_elements(request):
    return render(request, "basic_elements.html")

def chartjs(request):
    return render(request, "chartjs.html")

def mdi(request):
    return render(request, "mdi.html")

def error_404(request):
    return render(request, "error_404.html")

def error_500(request):
    return render(request, "error_500.html")

def form(request):
    return render(request, "form.html")

def view_data(request):
    return render(request, "view_data.html")

def save_data(request):
    if request.method == 'POST':
        user = request.POST["user"]
        # print(user)
        product =  request.POST["product"]
        # print(product)
        sales = request.POST["sales"]
        # print(sales)
        amount = request.POST["amount"]
        # print(amount)

        tables = details_table(user=user, product=product, sales=sales, amount=amount)
        tables.save()
        return render(request, "form.html")
    return render(request, "form.html")


def view_data(request):
    data = details_table.objects.all()
    print(data,'This is data')
    return render(request, "view_data.html", {'data':data})

def update_page(request, id):
    if request.method == "POST":
        user = request.POST["user"]
        product = request.POST["product"]
        sales = request.POST["sales"]
        amount = request.POST["amount"]
        data = details_table.objects.get(id=id)
        data.user = user
        data.product = product
        data.sales = sales
        data.amount = amount
        data.save()
        data = details_table.objects.all()
        print(data,'This is data')
        return render(request, "view_data.html", {'data':data})
    else:
        data = details_table.objects.get(id=id)
        print(data)
        return render(request, "update_page.html", {'data':data})
    
def delete(request, id):
    data = details_table.objects.get(id=id)
    data.delete()
    data1 = details_table.objects.all()
    print(data,'This is data')
    return render(request, "view_data.html", {'data':data1})


def delete_multiple_items(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_items')  # Get list of selected IDs
        details_table.objects.filter(id__in=selected_ids).delete()  # Delete selected items
        data1 = details_table.objects.all()
        
        return render(request, "view_data.html", {'data':data1})
    












# def update_person(request, person_id):
#     person = get_object_or_404(Person, id=person_id)  # Fetch the specific record
#     if request.method == "POST":
#         form = PersonForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()  # Save changes to the database
#             return redirect('display_data')  # Redirect to a data display page
#     else:
#         form = PersonForm(instance=person)  # Populate the form with the existing data
#     return render(request, 'update_person.html', {'form': form})
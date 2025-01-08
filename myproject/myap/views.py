from django.shortcuts import render, redirect
from .models import details_table, register_table
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from functools import wraps
from datetime import datetime
from django.db.models import Q




# Create your views here.
def session_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not request.session.get('is_logged_in'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapped_view

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # print(username)
        email = request.POST['email']
        # print(email)
        # country = request.POST['country']
        # print(country)
        password = request.POST['password']
        # print(password)

        if register_table.objects.filter(username=username).exists():
            messages.error(request,"Username already exist.")
            return redirect('login')
        
        registers = register_table(username=username, email=email, password=password)
        registers.save()
        messages.success(request, 'Registration successful Please log in.')
        return redirect("login")
    
    return render(request, "register.html")

def login(request):
    # print('Login function')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["password"]
        # print(username,password)

        try:
            # print('try block')
            user = register_table.objects.get(username=username)
            if user.password == password:
                request.session['username']=username
                request.session['is_logged_in'] = True
                # print('try condition if statement')
                return redirect("dashboard")
            else:
                # print('try condition else statement')
                messages.error(request,"Invalid password.")
        except register_table.DoesNotExist:
            # print('except block')
            messages.error(request, "User not found.")
            
    return render(request, "login.html")

@session_required
def logout(request):
    request.session.flush()
    return redirect('login')

@session_required
def dashboard(request):
    # username_r = request.session.get('username')
    # return render(request, "dashboard.html" /*, {'username':username_r}*/ )
    return render(request, "dashboard.html")

@session_required
def table(request):
    return render(request, "table.html")

@session_required
def buttons(request):
    return render(request, "buttons.html")

@session_required
def dropdowns(request):
    return render(request, "dropdowns.html")

@session_required
def typography(request):
    return render(request, "typography.html")

@session_required
def basic_elements(request):
    return render(request, "basic_elements.html")

@session_required
def chartjs(request):
    return render(request, "chartjs.html")

@session_required
def mdi(request):
    return render(request, "mdi.html")

@session_required
def error_404(request):
    return render(request, "error_404.html")

@session_required
def error_500(request):
    return render(request, "error_500.html")

@session_required
def form(request):
    return render(request, "form.html")

@session_required
def view_data(request):
    return render(request, "view_data.html")

@session_required
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
        username=request.session["username"]
        cur_date = datetime.now().date()
        cur_time = datetime.now().strftime('%H:%M:%S')
        # print(cur_date,'This is date')
        # print(cur_time,'This is time')

        tables = details_table(user=user, product=product, sales=sales, amount=amount, username=username, cur_date=cur_date, cur_time=cur_time)
        print(tables,'This is tables')

        tables.save()
        return render(request, "form.html")
    return render(request, "form.html")

@session_required
def view_data(request):
    data = details_table.objects.all()
    # print(data,'This is data')
    # for i in data:
    #     print(i.user)
    #     print(i.cur_date)
    #     print(i.cur_time)
    # is_admin = request.user.is_staff
    search_query = request.GET.get('search', '')
    # data = details_table.objects.filter(user__icontains=search_query)
    # if search_query:
    data = details_table.objects.filter(
        Q(user__icontains=search_query) |
        Q(product__icontains=search_query) |
        Q(sales__icontains=search_query) |
        Q(amount__icontains=search_query) |
        Q(username__icontains=search_query)
        )
    # else:
    #     data = details_table.objects.all()
    return render(request, "view_data.html", {'data':data, 'search_query': search_query})

@session_required
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
        # print(data,'This is data')
        return render(request, "view_data.html", {'data':data})
    else:
        data = details_table.objects.get(id=id)
        # print(data)
        return render(request, "update_page.html", {'data':data})

@session_required
def delete(request, id):
    data = details_table.objects.get(id=id)
    data.delete()
    data1 = details_table.objects.all()
    # print(data,'This is data')
    return render(request, "view_data.html", {'data':data1})

@session_required
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
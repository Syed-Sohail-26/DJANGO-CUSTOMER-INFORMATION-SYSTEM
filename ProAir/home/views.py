from django.shortcuts import render, redirect

# Create your views here.
from home.models import Customer


def homepage(request):
    return render(request, 'home.html')


def disp_cust(request):
    all_cust_details = Customer.objects.all()
    print(all_cust_details)
    context = {
        'allstu': all_cust_details
    }

    return render(request, 'allstu.html', context)


def login(request):
    return render(request, 'login.html')


def save(request):
    if request.method == 'POST':
        st = Customer()
        st.name = request.POST['name']
        st.email = request.POST['email']
        st.mobile = request.POST['mob']
        st.uname = request.POST['un']
        st.pwd = request.POST['pw']
        st.save()
        return redirect("/display/customers/")
    else:
        return render(request, 'regform.html')


def delete(request, id):
    print("Delete is delete method ", id)
    stu_details = Customer.objects.get(id=id)
    stu_details.delete()
    return redirect("/display/customers/")


def update(request, id):
    print("this is Update method ", id)
    stu_details = Customer.objects.get(id=id)
    context = {
        'id': stu_details.id,
        'name': stu_details.name,
        'email': stu_details.email,
        'mobile': stu_details.mobile,
    }
    return render(request, 'updform.html', context)


def update_result(request):
    st = Customer()
    st.id = request.POST['id']
    st.name = request.POST['name']
    st.email = request.POST['add']
    st.mobile = request.POST['mob']
    st.save()
    return redirect('/display/customers/')


def loginprocess(request):
    uname = request.POST['uname']
    pwd = request.POST['pwd']
    print(uname, pwd)
    stuobj = Customer.objects.filter(uname=uname) & Customer.objects.filter(pwd=pwd)
    print(stuobj)
    if uname == 'admin' and pwd == '1234':
        context = {'msg2': 'Admin Login Success'}
        print("Admin Login Success")
        return redirect('/display/customers/')
    elif stuobj:
        context = {'msg2': 'Login Success'}
        print("Login Success")
        return render(request,'home.html', context)
    else:
        context = {'msg1': 'Username or password invalid'}
        print("Username or password invali")
        return render(request , 'login.html', context)


def search(request):
    return render(request, 'search.html')


def serprocess(request):
    search = request.POST['ser']
    stuobj = Customer.objects.filter(name__icontains=search)
    if not stuobj:
        context = {'msg1': 'Customer not found'}
        print("Customer not found")
        return render(request, 'search.html', context)
    else:

        print("Customer found")
        print(stuobj[0].name)
        context = {
            'id': stuobj[0].id,
            'name': stuobj[0].name,
            'email': stuobj[0].email,
            'mobile': stuobj[0].mobile,
        }
        return render(request, 'serstu.html', context)

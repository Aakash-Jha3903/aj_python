from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.urls import reverse

# from Django_GS.CRUD_GS.enroll_app.forms import StudentRegistration
from .forms import StudentRegistration

from .models import User
# Create your views here.

# Add new data and Display all data............


def add_show(request):
    if request.method == 'POST':
        # "request.POST" is very important
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            # reg = User(name=nm,email=em)  # password will NOT be saved in DB!!
            reg.save()
            # (not good practice) Blank form for templates AND prevents multiple refresh form-submission
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()     # blank form from the GET method
    # fm = StudentRegistration()      # NOT blank form
    student_data = User.objects.all()

    dic = {
        "form": fm,
        "student_data": student_data
    }
    return render(request, "enroll/addAndShow.html", dic)


# Delete the data
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        del_dict = {
            "del_msg": "Data Deleted Successfully!!"
            # "msg": f" {} Deleted Successfully!!"
        }
        """request.session['del_msg'] = "Data Deleted Successfully!!"
        return redirect('/')"""
        return HttpResponseRedirect('/')
        # return redirect(request.META.get('HTTP_REFERER', '/'))
        # return HttpResponseRedirect(request, 'enroll/addAndShow.html',del_dict)

        # return redirect('/?del_msg=Data%20Deleted%20Successfully!!')


# Updates the Data
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)

        if fm.is_valid():   # if fm.is_valid:
            fm.save()
            fm = StudentRegistration()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    dic_upd = {
        "id": id,
        "form": fm
    }
    return render(request, 'enroll/updatestudent.html', dic_upd)


# else:

#     print(fm.errors)

#     return HttpResponse("Error")  #

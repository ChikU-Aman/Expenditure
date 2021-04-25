from django.shortcuts import render, HttpResponseRedirect
from .forms import Expense
from .models import User
import csv
# Create your views here.
spend = True
def add_show(request):
    if request.method == 'POST':
        fm = Expense(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Expense()
    else:
        fm = Expense()
    total = User.objects.all()
    sum_ = 0
    for i in total:
        sum_+=i.amount
    global spend
    spend = sum_ 
    if spend==True:
        flag = True
        return render(request,'main/add&show.html',{'form': fm,'al':total,'s':spend,'f':flag})
    else:
        flag = False
        return render(request,'main/add&show.html',{'form': fm,'al':total,'s':spend,'f':flag})
#this delete tuple
def delete(request,id):
    if request.method == "POST":
        p = User.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect('/')

#this function update tuple
def update(request,id):
    if request.method == "POST":
        p = User.objects.get(pk=id)
        fm = Expense(request.POST, instance=p)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = Expense(instance=pi)
    return render(request,'main/update.html',{'form':fm})

def export(request):
    if request.method == "POST":
        files = User.objects.all()
        filename = "expenditure.csv"
        f = open(filename,"w")
        headers = "S.No., Name, Date, Amount, Note"
        f.write(headers)
        f.write("\n")
        j = 1
        for i in files:
            f.write(str(j))
            f.write(',')
            f.write(i.name)
            f.write(',')
            f.write(str(i.date))
            f.write(',')
            f.write(str(i.amount))
            f.write(',')
            f.write(i.note)
            f.write("\n")
            j+=1
        f.close()
    return HttpResponseRedirect('/')
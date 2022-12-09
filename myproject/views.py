from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from myapp.models import Link

def Getlink(request):
    if request.method =="POST":
        site = request.POST.get('site','')

        page=requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')


        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address = link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data= Link.objects.all()

        
    

    return render(request,'index.html',{'data':data})

def delete(requet):
    Link.objects.all().delete()
    return render(requet,'index.html')

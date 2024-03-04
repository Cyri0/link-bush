from django.shortcuts import render
from .models import MyLink
from django.contrib.auth.models import User
# Create your views here.


# http://localhost:8000/page/admin
# http://localhost:8000/page/teszt_elek

def getPageByUser(request, username):
    user = User.objects.get(username=username)
    if user is not None:
        links = MyLink.objects.filter(user = user, visible = True)
        return render(request, 'page.html', {'links':links})
    return render(request, 'page.html', {'msg':"Valami nem király..."})
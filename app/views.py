from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request)

def cd(request):
    return render(request)

def sirch(request):
    return render(request)

def bd(request):
    return render(request)

def personal(request):
    return render(request)

def hack(request):
    return render(request)

def volunteer(request):
    return render(request)

def bloomTech(request):
    return render(request)

def microsoft(request):
    return render(request)



def logReg(request):
    return render(request)

def logout(request):
    pass

def login(request):
    pass

def register(request):
    pass

def adminDash(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)




def createMain(request):
    pass

def editMain(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updateMain(request):
    pass

def deleteMain(request):
    pass




def createHome(request):
    pass

def editHome(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updateHome(request):
    pass

def deleteHome(request):
    pass



def createWork(request):
    pass

def editWork(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updateWork(request):
    pass

def deleteWork(request):
    pass




def createPersonal(request):
    pass

def editPersonal(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updatePersonal(request):
    pass

def deletePersonal(request):
    pass




def createLearning(request):
    pass

def editLearning(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updateLearning(request):
    pass

def deleteLearning(request):
    pass
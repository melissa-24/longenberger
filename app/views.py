from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    work = Link.objects.filter(page=1,theType=1,topic=1).order_by('order')
    social = Link.objects.filter(page=1, theType=1, topic=2).order_by('order')
    weather = Link.objects.filter(page=1, theType=1, topic=3).order_by('order')
    context = {
       'work': work,
       'social': social,
       'weather': weather, 
    }
    return render(request, 'index.html', context)

def cd(request):
    cohort = Link.objects.filter(page=2,theType=1).order_by('order')
    admin = Link.objects.filter(page=2, theType=2).order_by('order')
    misc = Link.objects.filter(page=2, theType=3).order_by('order')
    context = {
        'cohort': cohort,
        'admin': admin,
        'misc': misc
    }
    return render(request, 'work/codingDojo.html', context)

def sirch(request):
    tasks = Link.objects.filter(page=2,theType=1).order_by('order')
    work = Link.objects.filter(page=2, theType=2).order_by('order')
    context = {
        'tasks': tasks,
        'work': work,
    }
    return render(request, 'work/sirch.html', context)

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
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'admin/logReg.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/dashboard/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/')

def register(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/logReg/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/dashboard/')

def adminDash(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'page': Page.objects.all().values(),
        'theType': Type.objects.all().values(),
        'topic': Topic.objects.all().values(),
        'user': user,
    }
    return render(request, 'admin/dash.html', context)




def createPage(request):
    Page.objects.create(
        page = request.POST['page']
    )
    return redirect('/dashboard/')

def editPage(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updatePage(request):
    pass

def deletePage(request):
    pass




def createType(request):
    Type.objects.create(
        theType = request.POST['theType']
    )
    return redirect('/dashboard/')

def editType(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updateType(request):
    pass

def deleteType(request):
    pass



def createTopic(request):
    Topic.objects.create(
        topic = request.POST['topic']
    )
    return redirect('/dashboard/')

def editTopic(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updateTopic(request):
    pass

def deleteTopic(request):
    pass




def createLink(request):
    Link.objects.create(
        url = request.POST['url'],
        name = request.POST['name'],
        page_id = request.POST['page'],
        theType_id = request.POST['theType'],
        topic_id = request.POST['topic'],
        order = request.POST['order']
    )
    return redirect('/dashboard/')

def editLink(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request)

def updateLink(request):
    pass

def deleteLink(request):
    pass


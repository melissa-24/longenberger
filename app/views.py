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
    cohort = Link.objects.filter(page=2,theType=2).order_by('order')
    admin = Link.objects.filter(page=2, theType=3).order_by('order')
    misc = Link.objects.filter(page=2, theType=4).order_by('order')
    context = {
        'cohort': cohort,
        'admin': admin,
        'misc': misc
    }
    return render(request, 'work/codingDojo.html', context)

def sirch(request):
    tasks = Link.objects.filter(page=2,theType=5).order_by('order')
    work = Link.objects.filter(page=2, theType=6).order_by('order')
    context = {
        'tasks': tasks,
        'work': work,
    }
    return render(request, 'work/sirch.html', context)

def bd(request):
    services = Link.objects.filter(page=2,theType=7).order_by('order')
    classroom = Link.objects.filter(page=2,theType=8).order_by('order')
    themes = Link.objects.filter(page=2,theType=9).order_by('order')
    important = Link.objects.filter(page=2,theType=10).order_by('order')
    context = {
        'services': services,
        'classroom': classroom,
        'themes': themes,
        'important': important,
    }
    return render(request, 'work/beeDev.html', context)

def bloomTech(request):
    training = Link.objects.filter(page=3, theType=2).order_by('order')
    notes = Link.objects.filter(page=3, theType=4).order_by('order')
    context = {
        'training': training,
        'notes': notes,
    }
    return render(request, 'learning/lambda.html', context)

def microsoft(request):
    dojo = Link.objects.filter(page=3, theType=6).order_by('order')
    training = Link.objects.filter(page=3, theType=8).order_by('order')
    context = {
        'dojo': dojo,
        'training': training,
    }
    return render(request, 'learning/microsoft.html', context)

def scotch(request):
    markup = Link.objects.filter(page=3, theType=11).order_by('order')
    javaScript = Link.objects.filter(page=3, theType=12).order_by('order')
    react = Link.objects.filter(page=3, theType=13).order_by('order')
    python = Link.objects.filter(page=3, theType=14).order_by('order')
    context = {
        'markup': markup,
        'javaScript': javaScript,
        'react': react,
        'python': python,
    }
    return render(request, 'learning/scotch.html', context)

def schools(request):
    coding = Link.objects.filter(page=3, theType=15).order_by('order')
    misc = Link.objects.filter(page=3, theType=1)
    context = {
        'coding': coding,
        'misc': misc,
    }
    return render(request, 'learning/schools.html', context)

def volunteer(request):
    services = Link.objects.filter(page=5, theType=7).order_by('order')
    general = Link.objects.filter(page=5, theType=4).order_by('order')
    context = {
        'services': services,
        'general': general,
    }
    return render(request, 'coding/volunteer.html', context)

def hack(request):
    hackathons = Link.objects.filter(page=5, theType=15).order_by('order')
    challenges = Link.objects.filter(page=5, theType=8).order_by('order')
    context = {
        'hackathons': hackathons,
        'challenges': challenges,
    }
    return render(request, 'coding/hackathons.html', context)

def websites(request):
    misc = Link.objects.filter(page=5, theType=1).order_by('order')
    web = Link.objects.filter(page=5, theType=12).order_by('order')
    context = {
        'misc': misc,
        'web': web,
    }
    return render(request, 'coding/websites.html', context)



def logReg(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'admin/logReg.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    if not User.objects.authenticate(request.POST['username'], request.POST['password']):
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    user = User.objects.get(username = request.POST['username'])
    request.session['user_id'] = user.id
    return redirect('/dashboard/')

def register(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/logReg/')
    newUser = User.objects.register(request.POST)
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
        'links': Link.objects.all().values(),
        'user': user,
    }
    return render(request, 'admin/dash.html', context)




def createPage(request):
    Page.objects.create(
        page = request.POST['page']
    )
    return redirect('/dashboard/')

def editPage(request, page_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        edit = Page.objects.get(id=page_id)
        context = {
            'user': user,
            'edit': edit,
        }
        return render(request, 'admin/editPage.html', context)

def updatePage(request, page_id):
    toUpdate = Page.objects.get(id=page_id)
    toUpdate.page=request.POST['page']
    toUpdate.save()
    return redirect(f'/theAdmin/page/{page_id}/edit/')

def deletePage(request, page_id):
    toDelete = Page.objects.get(id=page_id)
    toDelete.delete()
    return redirect('/dashboard')




def createType(request):
    Type.objects.create(
        theType = request.POST['theType']
    )
    return redirect('/dashboard/')

def editType(request, type_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        edit = Type.objects.get(id=type_id)
        context = {
            'user': user,
            'edit': edit,
        }
        return render(request, 'admin/editType.html', context)

def updateType(request, type_id):
    toUpdate = Type.objects.get(id=type_id)
    toUpdate.theType=request.POST['theType']
    toUpdate.save()
    return redirect(f'/theAdmin/type/{type_id}/edit/')

def deleteType(request, type_id):
    toDelete = Type.objects.get(id=type_id)
    toDelete.delete()
    return redirect('/dashboard')



def createTopic(request):
    Topic.objects.create(
        topic = request.POST['topic']
    )
    return redirect('/dashboard/')

def editTopic(request, topic_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        edit = Topic.objects.get(id=topic_id)
        context = {
            'user': user,
            'edit': edit,
        }
        return render(request, 'admin/editTopic.html', context)

def updateTopic(request, topic_id):
    toUpdate = Topic.objects.get(id=topic_id)
    toUpdate.topic=request.POST['topic']
    toUpdate.save()
    return redirect(f'/theAdmin/topic/{topic_id}/edit/')

def deleteTopic(request, topic_id):
    toDelete = Topic.objects.get(id=topic_id)
    toDelete.delete()
    return redirect('/dashboard')




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

def editLink(request, link_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        edit = Link.objects.get(id=link_id)
        context = {
            'user': user,
            'edit': edit,
            'page': Page.objects.all().values(),
            'theType': Type.objects.all().values(),
            'topic': Topic.objects.all().values(),
        }
        return render(request, 'admin/editLink.html', context)

def updateLink(request, link_id):
    toUpdate = Link.objects.get(id=link_id)
    toUpdate.url=request.POST['url']
    toUpdate.name=request.POST['name']
    toUpdate.page=request.POST['page']
    toUpdate.theType=request.POST['theType']
    toUpdate.topic=request.POST['topic']
    toUpdate.order=request.POST['order']
    toUpdate.save()
    return redirect(f'/theAdmin/links/{link_id}/edit/')

def deleteLink(request, link_id):
    toDelete = Link.objects.get(id=link_id)
    toDelete.delete()
    return redirect('/dashboard')


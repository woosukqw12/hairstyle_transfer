from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.final_input_ver import *

# Create your views here.
def index(response):
	return HttpResponse("<h1>qwe</h1>")

def v1(request):
    '''
    conn = sqlite3.connect("test01.db")
    cur = conn.cursor()
    data = cur.execute("select * from test01")
    return HttpResponse("<h1>%s</h1>" %data)
    '''
    photo1  = "../Resulted_edgesam.jpg"
    photo2 = "../Resulted_temsam.jpg"

    return render(request, 'main/pictures.html', {'photo1': photo1, 'photo2': photo2})

def v2(response, inputed):
	return HttpResponse("<h2>it's v2! %s</h2>" %inputed)
    
@csrf_exempt
def v3(request):
    '''
    photo = "images/Board4.jpg"
    javalink = "./javascripts/photo.js"
    csslink = "./stylesheets/main.css"
    return render(request, 'main/webcam.html', {'photo': photo, 'javalink': javalink, 'csslink':csslink})
    '''
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name

            #fp = open('%s/%s' % ('/Users/woosuk/djangoProjects/mysite_fix/mysite_jiho/main/templates/main/images', filename) , 'wb')
            fp = open('%s/%s' % ('/Users/woosuk/_PROJECTS/djangoProjects/mysite_fix/mysite_woo', filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            play('%s' %filename)
            #return HttpResponse('File Uploaded %s' %filename)
            return render(request, 'main/pictur.html')
    return HttpResponse('Failed to Upload File')


def v4(request):
    return render(request, 'main/webcam_ex.html')

def index(request):
    message = 'pages'
    photo = "images/Board4.jpg" #'images/Resulted_edgesam.jpg'
    photo1  = "images/Resulted_edgesam.jpg"
    photo2 = "images/Resulted_temsam.jpg"

    return render(request, 'main/index.html', {'message': message, 'photo': photo, 'photo1': photo1, 'photo2': photo2})
'''
def upload(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name

            fp = open('%s/%s' % ('main/images/', filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            return HttpResponse('File Uploaded')
    return HttpResponse('Failed to Upload File')

'''

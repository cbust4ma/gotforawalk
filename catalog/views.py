from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

#push 
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import firebase_admin

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    return render(
        request,
        'index.html'
       )
def event(request):
    return render(request,'event.html')
def bookmarks (request):
    return render(request,'bookmarks.html')

def service_worker(request):
    sw_path = settings.BASE_DIR / "catalog" / "static/js" / "sw.js"
    response = HttpResponse(open(sw_path).read(), content_type='application/javascript')
    return response

def service_fire(request):
    fire_path = settings.BASE_DIR / "catalog" / "static" / "firebase-messaging-sw.js"
    response = HttpResponse(open(fire_path).read(), content_type='application/javascript')
    return response
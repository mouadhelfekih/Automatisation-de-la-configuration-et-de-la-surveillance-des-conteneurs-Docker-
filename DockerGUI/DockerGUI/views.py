
from revproxy.views import ProxyView
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.conf import settings
from app.models import Objet
from .serializers import ObjetSerializer , renameSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .script_py.DockerGUI import *
from .script_py.dockergen import Dockergen
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator


class PsList(APIView):

    def post(self, request, format=None):
        d=[]
        desc=[]
        usr=request.data["username"][0:]

        o=Objet.objects.filter(username__username = usr)
        p=Conteneurs.ps()
        for i in o :
            d.append(i.id_conteneur)
        for i in p :
            if i['Id'] in d :
                desc.append(i)
        return Response(desc)
@method_decorator(csrf_exempt, name='dispatch')
class Conteneurs_run(APIView):
    def post(self, request, format=None):
            oid=request.data["id_image"]
            usr=request.data["username"][0:]
            p=Conteneurs.run(oid)
            a=p[:12]
            usr=User.objects.get(username=usr)
            cont=Objet(id_image=oid,id_conteneur=a ,username=usr)
            cont.save()
            return Response("bien")

class Conteneurs_logs(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
            return Response(Conteneurs.logs(request.data["id_conteneur"]))

class Conteneurs_pause(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_conteneur"]
        Conteneurs.pause(oid)
        return Response("bien")

class Conteneurs_rm(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_conteneur"]
        Conteneurs.rm(oid)
        Objet.objects.filter(id_conteneur=oid).delete()
        return Response("bien")

class Conteneurs_unpause(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_conteneur"]
        Conteneurs.unpause(oid)
        return Response("bien")

class Conteneurs_rename(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_conteneur"]
        name=request.data["name"]
        Conteneurs.rename(oid,name)
        return Response("bien")



class Conteneurs_rm_stopped(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request , format=None):
        p=Conteneurs.ps()
        usr=request.data["username"][0:]
        print (usr)
        o=Objet.objects.filter(username__username=usr)
        oid=[]
        for i in o :
            for j in p :
                if i.id_conteneur==j['Id']:
                    if "Exited" in j['Status']:
                        print("1")
                        Conteneurs.rm(j['Id'])
                        Objet.objects.filter(id_conteneur=j['Id']).delete()
        return Response("bien")



class Conteneurs_restart(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_conteneur"]
        Conteneurs.restart(oid)
        return Response("bien")


class Conteneurs_start(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):

            oid=request.data["id_conteneur"]
            Conteneurs.start(oid)
            return Response("bien")


class Conteneurs_stats(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_conteneur"]
        return Response(Conteneurs.stats(oid))

class Conteneurs_stop(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_conteneur"]
        Conteneurs.stop(oid)
        return Response("bien")

class Conteneurs_top(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_conteneur"]
        return Response(Conteneurs.top(oid))

class Images_history(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        oid=request.data["id_image"]
        return Response(Images.history(oid))


class Conteneurs_build(APIView):

    def post(self,request,format=None):
        Base=request.data["base"]
        ocommande=request.data["command"]
        oPaquet=request.data["dependences"]
        oFichier=request.data["file"]
        usr=request.data["username"][0:]
        tag=request.data["tag"]
        opath="./static/"+usr
        print (opath)
        print(Base+usr+ocommande+oPaquet+oFichier+tag)
        try:
            os.mkdir(opath)
        except OSError:
            pass

        if oFichier=='' :
            Fichier=[]
        else :
            Fichier=oFichier.split(",")
        print(Fichier)
        if oPaquet=='' :
            Paquet=[]
        else :
            Paquet=oPaquet.split(",")
        print(Paquet)
        Dockergen.gen(Base,ocommande,Paquet,Fichier,usr)
        k=Images.build("/home/mouadh/Bureau/DockerGUI/static/"+usr,tag)
        a=dict(eval(k))["stream"][19:32]
        usr=User.objects.get(username=usr)
        cont=Objet(id_image=a ,username=usr)
        cont.save()
        return Response("hello")


class Images_images(APIView):

    def post(self,request,fromat=None):
        d=[]
        desc=[]
        usr=request.data["username"][0:]
        o=Objet.objects.filter(username__username = usr)
        p=Images.images()
        for i in o :
            d.append(i.id_image[:12])
        print (d)
        for i in p :
            print (i['Id'] )
            if i['Id'] in d :
                desc.append(i)

        return Response(desc)

class Images_pull(APIView):
    @method_decorator(csrf_exempt)
    def post(self,request,fromat=None):
        orepository=request.data["repository"]
        oid=Images.pull(orepository)[7:19]
        usr=request.data["username"][0:]
        print (usr)
        usr=User.objects.get(username=usr)
        cont=Objet(id_image=oid ,username=usr)
        cont.save()
        return Response("bien")


class Images_remove_image(APIView) :
    @method_decorator(csrf_exempt)
    def post(self,request,fromat=None):
        oid=request.data["id_image"]
        Images.remove_image(oid)
        Objet.objects.filter(id_conteneur=None,id_image=oid).delete()
        return Response("bien")
class Images_search(APIView) :
    @method_decorator(csrf_exempt)
    def post(self,request,fromat=None) :
        orepository=request.data["repository"]
        return Response (Images.search(orepository))
class Images_tag(APIView) :
    @method_decorator(csrf_exempt)
    def post(self,request,fromat=None) :
        oimage=request.data["id_image"]
        orepository=request.data["repository"]
        otag=request.data["tag"]
        Images.tag(oimage,orepository,otag)
        return Response("bien")




@api_view(['GET', 'POST', ])
def sess(request):
    user = request.user

    return Response(user.username)

class TestProxyView(ProxyView):
    upstream = 'http://localhost:4200'
    add_remote_user = True

    def get_proxy_request_headers(self, request):
        # Call super to get default headers
        headers = super(TestProxyView, self).get_proxy_request_headers(request)
        # Add new header
        #headers['userid'] = request.user.id
        return headers

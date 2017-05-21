import docker
import datetime
import json


class Conteneurs:


    def ps(oquie=False,oall=True,otrunc=False,olatest=False,olimit=-1, osize=False):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        Id=[]
        Image=[]
        Command=[]
        Created=[]
        Status=[]
        Ports=[]
        Names=[]
        ops=client.containers(quiet=oquie, all=oall,trunc=otrunc,latest=olatest,since=None,before=None,limit=olimit,size=osize,filters=None)

        for i in ops:

            Id.append(i['Id'][:12])
            Image.append(i['Image'])
            Command.append(i['Command'])
            cre=datetime.datetime.fromtimestamp( i['Created']).strftime('%Y-%m-%d ')
            Created.append(cre)
            Status.append(i['Status'])
            Ports.append(i['Ports'])
            Names.append(i['Names'])

        desc2=[]
        j=0
        while j<len(Id):
            desc2.append({'Id':Id[j],'Image':Image[j],'Command':Command[j],"Created":Created[j],"Status":Status[j],"Ports":Ports[j],"Names":Names[j]})
            j+=1
        return desc2


    def run(oimage, ocommand=None, omem_limit=None ,oname=None , ostop_timeout=None):

        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        p=client.create_container(oimage, command=ocommand,
          mem_limit=omem_limit,  name=oname, stop_timeout=ostop_timeout)
        return p['Id']

    def logs(ocontainer ,otail='all',osince=30):
        u=""
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        l=str(client.logs(ocontainer,  tail=otail, since=osince)).split("\\n")
        resp=[]
        for i in l:
            resp.append({"".join(i).replace("\\t","	").replace("\\r","")})
        return resp




    def pause(container):

        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.pause(container)

    def rm_stoped() :
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.prune_containers()

        #insert un ficjer tar dans un container (le path est le path dans le container)

    def insert(ocontainer,opath,odata):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.put_archive(container=ocontainer, path=opath, data=odata)

        #jamais supprimer un contenaire paused

    def rm(ocontainer):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.remove_container(container=ocontainer, v=True,  force=True)

    def rename(ocontainer, oname):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.rename(container=ocontainer,name=oname)

    def restart(ocontainer):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.restart( container=ocontainer , timeout = 10 )

    def start(ocontainer):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.start(container=ocontainer)
     #il faut que le statut de contenaire est up

    def stats(ocontainer):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        p=client.stats( container=ocontainer, decode=None, stream=True)
        k=0 ;
        for i in p:
            if k==0:
                u=i.decode('utf8')

                k+=1
            else :
                break
        try:
            k=(u.find("memory_stats"))
            h=k+23
            k+=23
            while h<len(u) :
                if u[h]==',':
                    break
                h+=1
            memory_stats=int(u[k:h])

            k=(u.find("precpu_stats"))
            h=k+42
            k+=42
            while h<len(u) :
                if u[h]==',':
                    break
                h+=1
            cpu_usage=int(u[k:h])

            k=(u.find("limit"))
            h=(u[k+5:len(u)].find("limit"))
            r=k+h+12
            while r<len(u) :
                if u[r]=='}':
                    break
                r+=1
            limit=int(u[k+h+12:r])

            por_mem=(memory_stats/limit)*100
            decs={ 'memory_stats': memory_stats, 'limit': limit, 'por_mem' :por_mem, 'cpu_usage' :cpu_usage}
        except :
            return ("votre conteneurs est stoped")

        return decs ;

    def stop(ocontainer):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.stop(container=ocontainer)

        #Afficher les processus en cours d'exécution d'un conteneur.

 #afficher les processus
    def top(ocontainer):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        try:
            s=client.top(container=ocontainer)
        except :
            return  ({"votre conteneurs est stoped"})
        return s["Processes"]

    def unpause(ocontainer):
        client = docker.APIClient(base_url='unix://var/run/docker.sock')
        client.unpause(container=ocontainer)



class Images :
    def history (oimage):
        client= docker.APIClient(base_url='unix://var/run/docker.sock')
        return client.history(image=oimage)

    def images() :
        client= docker.APIClient(base_url='unix://var/run/docker.sock')
        REPOSITORY=[]
        Id=[]
        Tags=[]
        Created=[]
        Size=[]
        ops=client.images()

        for i in ops:
            #print (i)
            Id.append(i['Id'][7:19])
            RepoTags=i['RepoTags'][0]
            k=0 ;
            while k<len(RepoTags):
                if RepoTags[k]==':' :
                    break ;
                k+=1


            Tags.append(RepoTags[k+1:len(RepoTags)])
            REPOSITORY.append(RepoTags[:k])
            cre=datetime.datetime.fromtimestamp( i['Created']).strftime('%Y-%m-%d ')
            Created.append(cre)
            Size.append(i['Size'])

        desc2=[]
        j=0
        while j<len(Id):
            desc2.append({'REPOSITORY':REPOSITORY[j],'Id':Id[j],'Tags':Tags[j],'Created':Created[j],'Size':Size[j] })
            j+=1
        return desc2

    #Delete unused images
    def prune_images():
        client= docker.APIClient(base_url='unix://var/run/docker.sock')
        client.prune_images() ,

    def pull(orepository):
        client = docker.from_env()
        im=orepository+":latest"
        image = client.images.pull(im)
        return (image.id)






    def push(orepository,otag=None) :
        client= docker.APIClient(base_url='unix://var/run/docker.sock')
        client.push(repository=orepository, tag=None, stream=True, insecure_registry=False, auth_config=None, decode=False)



    def remove_image(oimage):
        client= docker.APIClient(base_url='unix://var/run/docker.sock')
        client.remove_image(image=oimage, force=True, noprune=False)

    def search(oterm):
        client= docker.APIClient(base_url='unix://var/run/docker.sock')
        ovar=client.search(term=oterm)

        description=[]
        name=[]
        star_count=[]
        is_official=[]

        for i in ovar :
            description.append(i["description"])
            name.append(i["name"])
            star_count.append(i["star_count"])
            is_official.append(i["is_official"])


        desc2=[]
        j=0
        while j<len(description):
            desc2.append({'description':description[j],'name':name[j],'star_count':star_count[j],"is_official":is_official[j]})
            j+=1
        return desc2


    def tag(oimage, orepository,otag):
        client= docker.APIClient(base_url='unix://var/run/docker.sock')
        client.tag(image=oimage, repository=orepository, tag=otag, force=True)

    def build(opath,otag=None):
        client= docker.APIClient(base_url='unix://var/run/docker.sock')
        h=client.build(path=opath, tag=otag, pull=True,dockerfile=None)
        for i in h :
            pass
        u=i.decode('utf8')
        return (u)

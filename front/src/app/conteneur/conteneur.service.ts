import { CONTENEURS } from './conteneur.elements';
import { Injectable } from '@angular/core';
import { conteneur } from './conteneur';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { process } from './process'
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Injectable()
export class ConteneurService {
  constructor(private http:Http) {
  }

  postProcess(user,url,id):Observable<process[]> {
  var params = JSON.stringify({id_conteneur : id , username: user});
    var headers =  new Headers();
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{headers:headers})
        .map((res:Response) => res.json())
  }
  postJSON(user,url,id="",newName="")
  {
      var params = JSON.stringify({id_conteneur : id , username: user});
    if(newName!==""){
      params= JSON.stringify({id_conteneur : id , name : newName, username: user});
    }
    var headers =  new Headers();
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{ headers: headers })
        .map(res => res.json())
  }
  getConteneurs(user,url):Observable<conteneur[]> {
    var params= JSON.stringify({ username : user});
    var headers = new Headers();
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{headers:headers}).map((res:Response) => res.json()).catch(this.handleError);
  }
   private extractData(res: Response) {
    let body = res.json();
    return body.data || { };
  }

  private handleError (error: Response | any) {
  // In a real world app, you might use a remote logging infrastructure
  let errMsg: string;
  if (error instanceof Response) {
    const body = error.json() || '';
    const err = body.error || JSON.stringify(body);
    errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
  } else {
    errMsg = error.message ? error.message : error.toString();
  }
  console.error(errMsg);
  return Observable.throw(errMsg);
}
  getConteneur(id : string){
    var Conteneur : any;
    for (Conteneur of CONTENEURS)
    {
      if(Conteneur.id == id)
        return Conteneur;
    }
    }
  getJSON(user,url)
  {
    var params = JSON.stringify({ username: user});
    var headers = new Headers;
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{headers:headers}).map((res:Response) => res.json()).catch(this.handleError);
  }
}

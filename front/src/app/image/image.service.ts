import { Injectable } from '@angular/core';
import { image } from './image'
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Injectable()
export class ImageService {
  constructor(private http:Http) { }
  getImages(user):Observable<image[]> {
  var params = JSON.stringify({ username: user});
  var headers = new Headers();
  headers.append('Content-Type','application/json')
    return this.http.post('http://localhost:8000/images/?format=json',params, {headers: headers}).map((res:Response) => res.json()).catch(this.handleError);

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

postJSON(user,num,url){
  var params = JSON.stringify({id_image : num,username : user});
    var headers =  new Headers();
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{headers:headers})
        .map(res => res.json())
}
postSearch(user,num,url){
    var params = JSON.stringify({repository : num,username: user});
    var headers =  new Headers();
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{headers:headers})
        .map(res => res.json())
}
tagJSON(user,num,url,rep,newTag){
  var params = JSON.stringify({id_image : num , repository : rep , tag : newTag , username : user});
    var headers =  new Headers();
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{headers:headers})
        .map(res => res.json())
}
postDockerFile(user,url,tag,base,prenom_p,nom_p,email,dependences,commande,file){
    var params = JSON.stringify({tag:tag,base: base,prenom_p: prenom_p,nom_p: nom_p,email: email,dependences: dependences,
    command: commande, file: file , username:user});
    var headers =  new Headers();
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{headers:headers})
        .map(res => res.json())
}
}

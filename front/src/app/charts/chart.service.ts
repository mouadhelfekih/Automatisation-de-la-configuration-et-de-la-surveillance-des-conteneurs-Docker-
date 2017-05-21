import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
@Injectable()
export class ChartService {
  constructor(private http:Http) {
  }

  postStats(user,url,id) {
  var params = JSON.stringify({id_conteneur : id , username: user});
    var headers =  new Headers();
    headers.append('Content-Type','application/json');
    return this.http.post(url,params,{headers:headers})
        .map((res:Response) => res.json())
  }
  }

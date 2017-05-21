import { Cookie } from 'ng2-cookies';
import { Component, OnInit } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styles: [],
})
export class HeaderComponent implements OnInit {
  user:string;
  selectedId = 1;
  active(id){
    if (this.selectedId === id){
      return "active";
    }
      return "";
  }
  selectId(id){
    this.selectedId=id;
  }
  ngOnInit(){
    this.getUsername()
  }
  constructor(private http:Http) {
  }
  getUsername(){
    return this.http.get('http://127.0.0.1:8000/session/', { withCredentials: true }).map((res:Response) => res.json()).
    subscribe(data => this.user = data,
    () => {},
    () => console.log(this.user)
    );
  }
}

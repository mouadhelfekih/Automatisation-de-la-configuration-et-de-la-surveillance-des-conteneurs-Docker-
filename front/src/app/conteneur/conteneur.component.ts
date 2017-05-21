import { Response } from '@angular/http';
import { SearchPipe } from './../search.pipe';
import { ConteneurService } from './conteneur.service';
import { Component, OnInit, Pipe, Input } from '@angular/core';
import { conteneur } from './conteneur';
import { process } from './process'
import { ActivatedRoute } from '@angular/router'
@Component({
  selector: 'app-conteneur',
  templateUrl: './conteneur.component.html',
  styleUrls: ['./conteneur.component.css'],
  providers:[ConteneurService],
})
export class ConteneurComponent implements OnInit {
  public conteneurs:conteneur[];
  mode = 'Observable';
  newName:string;
  errorMessage: string;
  getData=[];
  logs:string;
  processes:Array<process>;
  stats:[{}];
  selectConteneur:string;
  user:string;
  constructor(private _ConteneurService: ConteneurService , private params: ActivatedRoute){
    this.params.params.subscribe(params => {
    this.user = params['user'];
    });
  }
  ngOnInit(){
    this.getConteneurs();
  }

  getConteneurs(){
  this._ConteneurService.getConteneurs(this.user,'http://localhost:8000/ps/').subscribe(conteneurs => this.conteneurs = conteneurs,
    () => {},
    () => console.log(this.conteneurs)
    );
  }
  getLogs(num)
  {
    this._ConteneurService.postJSON(this.user,'http://localhost:8000/logs/',num).subscribe(data => this.logs = data ,
    () => {},
    ()=> console.log(this.logs)
    );
  }
  confId: string;
  getConteneur(id:string){
    this.selectConteneur = id;
    console.log(id);
  }

  getProcess(num)
    {
      this._ConteneurService.postProcess(this.user,'http://localhost:8000/top/',num).subscribe(data => this.processes = data ,
      () => {},
      ()=> console.log(this.processes)
      );
    }
  startConteneur(num)
  {
    this._ConteneurService.postJSON(this.user,'http://localhost:8000/start/',num).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> {console.log("finished");this.getConteneurs()}
    );
}
  pauseConteneur(num)
  {
    this._ConteneurService.postJSON(this.user,'http://localhost:8000/pause/',num).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> {console.log("finished");this.getConteneurs()}
    );
  }

  restartConteneur(num)
  {
    this._ConteneurService.postJSON(this.user,'http://localhost:8000/restart/',num).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> { console.log("finished");this.getConteneurs()}
    );

}
  stopConteneur(num)
  {
    this._ConteneurService.postJSON(this.user,'http://localhost:8000/stop/',num).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> {console.log("finished");this.getConteneurs()}
    );
   }
  unpauseConteneur(num)
  {
    this._ConteneurService.postJSON(this.user,'http://localhost:8000/unpause/',num).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=>{console.log("finished");this.getConteneurs()}
    );
 }
  renameConteneur(num,fname)
  {
     this._ConteneurService.postJSON('this.user,http://localhost:8000/rename/',num,fname).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> {console.log("renamed");this.getConteneurs()}
    );

  }
  rmConteneur(num){
         this._ConteneurService.postJSON(this.user,'http://localhost:8000/rm/',num).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> {console.log("removed");this.getConteneurs(); }
    );
  }
  rmStopped(){
    this._ConteneurService.postJSON(this.user,'http://localhost:8000/rmstopped/').subscribe(data => console.log(JSON.stringify(data)) ,
    () => {},
    () => {console.log("removed");this.getConteneurs(); }
    );
  }

}

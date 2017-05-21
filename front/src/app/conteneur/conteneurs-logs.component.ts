import { ConteneurService } from './conteneur.service';
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { conteneur } from "app/conteneur/conteneur";

@Component({
  selector: 'app-conteneurs-logs',
  templateUrl: './conteneurs-logs.component.html',
  styles: [],
  providers:[ConteneurService]
})
export class ConteneursLogsComponent implements OnInit {
  id:any;
  paramsSub:any;
  Conteneur: conteneur;
  logs:any;
  stats(id:string){return 'it works'};
  constructor(private _ConteneurService: ConteneurService,private activatedRoute: ActivatedRoute){}
  ngOnInit() {
  this.paramsSub = this.activatedRoute.params.subscribe(params => this.id =(params['id']));
  this.Conteneur=this._ConteneurService.getConteneur(this.id);
  this.logs=this.stats(this.Conteneur.Id);
  }

}

import { ConteneurService } from './conteneur.service';
import { CONTENEURS } from './conteneur.elements';
import { RouterModule } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute,Params } from '@angular/router'
import { conteneur} from './conteneur'
@Component({
  selector: 'app-conteneurs-details',
  templateUrl: './conteneurs-details.component.html',
  styles: [],
  providers:[ConteneurService]
})
export class ConteneursDetailsComponent implements OnInit {
  id:any;
  paramsSub:any;
  Conteneur: conteneur;
  constructor(private _ConteneurService: ConteneurService,private activatedRoute: ActivatedRoute) { }
  ngOnInit() {
  this.paramsSub = this.activatedRoute.params.subscribe(params => this.id =(params['id']));
  this.Conteneur=this._ConteneurService.getConteneur(this.id);
  }

}

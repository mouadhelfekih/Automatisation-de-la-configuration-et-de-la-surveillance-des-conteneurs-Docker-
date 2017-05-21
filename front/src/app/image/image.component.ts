import { ImageService } from './image.service';
import { Component, OnInit } from '@angular/core';
import { image } from './image'
import { FileUploader } from 'ng2-file-upload';
import { ActivatedRoute } from '@angular/router'

const URL = 'https://evening-anchorage-3159.herokuapp.com/api/';

@Component({
  selector: 'app-image',
  templateUrl: './image.component.html',
  styleUrls: ['./image.component.css'],
  providers:[ImageService],
})
export class ImageComponent implements OnInit{
  public Images:image[];
  searchConteneur:string;
  searchResult:[{ star_count: number,name: string,is_official: boolean,description: string}]
  selectImage : string;
  newTag: string;
  newRepository:string;
  postId: number;
  loading : boolean;
  user : string;
  tag:string;
   base: string;
   nom:string;
   prenom:string;
   email:string;
   dependences:string;
   file: string;
   command:"";
  url='http://localhost:8000';
  constructor(private _ImageService: ImageService , private params: ActivatedRoute){
    this.params.params.subscribe(params => {
    this.user = params['user'];
    });
  }
  ngOnInit(){
    this.getImages();
  }
  searchConteneurs(repository){
    this._ImageService.postSearch(this.user,repository,this.url+'/search/').subscribe(data => this.searchResult = data ,
    () => {},
    ()=> console.log(this.searchResult)
    );
  }
  telechargerConteneur(repository){
    this.loading= true
    this._ImageService.postSearch(this.user,repository,this.url+'/pull/').subscribe(data => console.log(this.loading) ,
    () => {},
    ()=>{this.loading = false;this.getImages()}
    );
  }

  getImages(){
  this._ImageService.getImages(this.user).subscribe(images => this.Images = images,
    () => {},
    () => console.log(this.Images)
    );
  }
  runConteneur(num)
  {
    this._ImageService.postJSON(this.user,num,this.url+'/run/').subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> console.log("created")
    );
  }
  rmImage(num)
  {
    this._ImageService.postJSON(this.user,num,this.url+'/remove/').subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> {console.log("removed");this.getImages()}
    );
  }
  tagImage(num,rep,tag)
  {
    this._ImageService.tagJSON(this.user,num,this.url+'/tag/',rep,tag).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> {console.log("tagged");this.getImages()}
    );
  }
  getImage(id:string){
    this.selectImage = id;
    console.log(id);
  }
  buildDockerFile(tag,base,prenom_p,nom_p,email,dependences,commande,file){

    this._ImageService.postDockerFile(this.user,this.url+'/build/',tag,base,prenom_p,nom_p,email,dependences,commande,file).subscribe(data => console.log(JSON.stringify(data)) ,
    error => alert(error),
    ()=> {console.log("removed");this.getImages()}
    );
  }
}

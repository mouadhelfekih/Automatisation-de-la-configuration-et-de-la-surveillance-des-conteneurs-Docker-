import { UPLOAD_DIRECTIVES } from 'ng2-file-uploader/ng2-file-uploader';
import { routing } from './app.routes';
import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { AppComponent } from './app.component';
import { ConteneurComponent } from './conteneur/conteneur.component';
import { ImageComponent } from './image/image.component';
import { HeaderComponent } from './header.component';
import { InfosComponent } from './infos/infos.component';
import { ConteneursDetailsComponent } from './conteneur/conteneurs-details.component';
import { ConteneursLogsComponent } from './conteneur/conteneurs-logs.component';
import { SearchPipe } from './search.pipe';
import {NgPipesModule} from 'ngx-pipes';
import {APP_BASE_HREF} from '@angular/common';
import { ChartsComponent } from './charts/charts.component';

@NgModule({
  declarations: [
    AppComponent,
    ConteneurComponent,
    ImageComponent,
    HeaderComponent,
    InfosComponent,
    ConteneursDetailsComponent,
    ConteneursLogsComponent,
    SearchPipe,
    ChartsComponent,
    
    
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    routing,
    NgPipesModule
  ],
  providers: [UPLOAD_DIRECTIVES, {provide: APP_BASE_HREF, useValue: '/ui'}],
  bootstrap: [AppComponent],
})


export class AppModule { }

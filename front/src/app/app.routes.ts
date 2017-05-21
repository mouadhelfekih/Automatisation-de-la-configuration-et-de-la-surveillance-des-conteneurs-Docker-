import { ConteneursLogsComponent } from './conteneur/conteneurs-logs.component';
import { ConteneursDetailsComponent } from './conteneur/conteneurs-details.component';
import { InfosComponent } from './infos/infos.component';
import { ImageComponent } from './image/image.component';
import { ConteneurComponent } from './conteneur/conteneur.component';
import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

export const routes:Routes=[
    { path :'' , redirectTo : '/infos' , pathMatch : 'full'},
    { path: 'infos' , component: InfosComponent},
    { path: 'conteneurs',children:[
        { path :'', component: ConteneurComponent},
        { path :'details/:id',component:ConteneursDetailsComponent},
        { path :'logs/:id' , component: ConteneursLogsComponent},
    ] },
    { path: 'images', component: ImageComponent }
];

export const routing: ModuleWithProviders = RouterModule.forRoot(routes);

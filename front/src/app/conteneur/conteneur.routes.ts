import { ConteneurComponent } from './conteneur.component';
import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

export const routes:Routes=[
    { path :'' , redirectTo : '/conteneurs' , pathMatch : 'full'},
    { path: '/:id' , component: ConteneurComponent},
];

export const routing: ModuleWithProviders = RouterModule.forRoot(routes);

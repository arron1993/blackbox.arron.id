import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from './auth/guards/auth.guard';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'sessions',
    pathMatch: 'full',
  },
  {
    path: 'auth',
    loadChildren: () =>
      import('./auth/auth-routing.module').then((m) => m.AuthRoutingModule),
  },
  {
    path: 'sessions',
    loadChildren: () =>
      import('./core/core-routing.module').then((m) => m.CoreRoutingModule),
    canActivate: [AuthGuard],
  },
  {
    path: 'fuel',
    loadChildren: () =>
      import('./fuel/fuel-routing.module').then((m) => m.FuelRoutingModule),
    canActivate: [AuthGuard],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CalcuatorComponent } from './fuel/pages/calcuator/calcuator.component';

const routes: Routes = [
  {
    path: "auth",
    loadChildren: () => import("./auth/auth-routing.module").then(m => m.AuthRoutingModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

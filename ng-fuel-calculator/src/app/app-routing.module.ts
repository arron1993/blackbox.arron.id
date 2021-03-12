import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CalcuatorComponent } from './fuel/pages/calcuator/calcuator.component';

const routes: Routes = [
  {
    path: "",
    component: CalcuatorComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

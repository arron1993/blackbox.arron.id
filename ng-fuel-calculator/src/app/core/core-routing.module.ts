import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CircuitListPageComponent } from './pages/circuit-list-page/circuit-list-page.component';

const routes: Routes = [
  {
    path: "",
    component: CircuitListPageComponent,
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CoreRoutingModule { }

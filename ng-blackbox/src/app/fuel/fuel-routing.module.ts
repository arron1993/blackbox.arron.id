import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CalcuatorComponent } from './pages/calcuator/calcuator.component';

const routes: Routes = [{ path: '', component: CalcuatorComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class FuelRoutingModule {}

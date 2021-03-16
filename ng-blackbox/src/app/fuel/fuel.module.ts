import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CalcuatorComponent } from './pages/calcuator/calcuator.component';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [CalcuatorComponent],
  imports: [
    CommonModule,
    FormsModule
  ]
})
export class FuelModule { }

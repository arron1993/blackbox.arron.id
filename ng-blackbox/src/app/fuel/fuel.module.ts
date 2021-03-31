import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CalcuatorComponent } from './pages/calcuator/calcuator.component';
import { FormsModule } from '@angular/forms';
import { FuelRoutingModule } from './fuel-routing.module';
import { CalculatorFieldComponent } from './components/calculator-field/calculator-field.component';

@NgModule({
  declarations: [CalcuatorComponent, CalculatorFieldComponent],
  imports: [CommonModule, FuelRoutingModule, FormsModule],
})
export class FuelModule {}

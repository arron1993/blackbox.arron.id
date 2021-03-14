import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CoreRoutingModule } from './core-routing.module';
import { DashboardPageComponent } from './pages/dashboard-page/dashboard-page.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CarListComponent } from './components/car-list/car-list.component';
import { SessionListComponent } from './components/session-list/session-list.component';
import { CircuitListComponent } from './components/circuit-list/circuit-list.component';


@NgModule({
  declarations: [DashboardPageComponent, CarListComponent, SessionListComponent, CircuitListComponent],
  imports: [
    CommonModule,
    CoreRoutingModule,
    HttpClientModule,
    FormsModule
  ]
})
export class CoreModule { }

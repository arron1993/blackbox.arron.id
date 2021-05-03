import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ChartsModule } from 'ng2-charts';

import { CoreRoutingModule } from './core-routing.module';
import { DashboardPageComponent } from './pages/dashboard-page/dashboard-page.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CarListComponent } from './components/car-list/car-list.component';
import { SessionListComponent } from './components/session-list/session-list.component';
import { CircuitListComponent } from './components/circuit-list/circuit-list.component';
import { SessionPageComponent } from './pages/session-page/session-page.component';
import { SessionTypeListComponent } from './components/session-type-list/session-type-list.component';
import { LapChartComponent } from './components/lap-chart/lap-chart.component';
import { LoadingSpinnerComponent } from './components/loading-spinner/loading-spinner.component';

@NgModule({
  declarations: [
    DashboardPageComponent,
    CarListComponent,
    SessionListComponent,
    CircuitListComponent,
    SessionPageComponent,
    SessionTypeListComponent,
    LapChartComponent,
    LoadingSpinnerComponent,
  ],
  imports: [
    CommonModule,
    CoreRoutingModule,
    HttpClientModule,
    FormsModule,
    ChartsModule,
  ],
  exports: [CarListComponent],
})
export class CoreModule {}

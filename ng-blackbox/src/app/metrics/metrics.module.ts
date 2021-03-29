import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MetricsRoutingModule } from './metrics-routing.module';
import { CircuitSummaryPageComponent } from './pages/circuit-summary-page/circuit-summary-page.component';
import { MetricDashboardPageComponent } from './pages/metric-dashboard-page/metric-dashboard-page.component';
import { CarGroupSelectorComponent } from './components/car-group-selector/car-group-selector.component';


@NgModule({
  declarations: [CircuitSummaryPageComponent, MetricDashboardPageComponent, CarGroupSelectorComponent],
  imports: [
    CommonModule,
    MetricsRoutingModule
  ]
})
export class MetricsModule { }

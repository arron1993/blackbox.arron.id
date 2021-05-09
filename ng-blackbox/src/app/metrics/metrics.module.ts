import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MetricsRoutingModule } from './metrics-routing.module';
import { CircuitSummaryPageComponent } from './pages/circuit-summary-page/circuit-summary-page.component';
import { MetricDashboardPageComponent } from './pages/metric-dashboard-page/metric-dashboard-page.component';
import { CarGroupSelectorComponent } from './components/car-group-selector/car-group-selector.component';
import { CarSummaryPageComponent } from './pages/car-summary-page/car-summary-page.component';
import { CoreModule } from '../core/core.module';
import { CarSummaryListComponent } from './components/car-summary-list/car-summary-list.component';
import { SplitLabelComponent } from './components/split-label/split-label.component';

@NgModule({
  declarations: [
    CircuitSummaryPageComponent,
    MetricDashboardPageComponent,
    CarGroupSelectorComponent,
    CarSummaryPageComponent,
    CarSummaryListComponent,
    SplitLabelComponent,
  ],
  imports: [CommonModule, MetricsRoutingModule, CoreModule],
})
export class MetricsModule {}

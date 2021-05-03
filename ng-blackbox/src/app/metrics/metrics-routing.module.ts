import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from '../auth/guards/auth.guard';
import { CarSummaryPageComponent } from './pages/car-summary-page/car-summary-page.component';
import { CircuitSummaryPageComponent } from './pages/circuit-summary-page/circuit-summary-page.component';
import { MetricDashboardPageComponent } from './pages/metric-dashboard-page/metric-dashboard-page.component';

const routes: Routes = [
  {
    path: '',
    component: MetricDashboardPageComponent,
    canActivate: [AuthGuard],
  },
  {
    path: 'circuits',
    component: CircuitSummaryPageComponent,
    canActivate: [AuthGuard],
  },
  {
    path: 'cars',
    component: CarSummaryPageComponent,
    canActivate: [AuthGuard],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MetricsRoutingModule {}

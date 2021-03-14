import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DashboardPageComponent } from './pages/dashboard-page/dashboard-page.component';
import { SessionPageComponent } from './pages/session-page/session-page.component';

const routes: Routes = [
  {
    path: "",
    component: DashboardPageComponent,
  }, {
      path: ":id",
      component: SessionPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CoreRoutingModule { }

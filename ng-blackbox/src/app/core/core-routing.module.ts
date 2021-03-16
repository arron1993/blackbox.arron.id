import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from '../auth/guards/auth.guard';
import { DashboardPageComponent } from './pages/dashboard-page/dashboard-page.component';
import { SessionPageComponent } from './pages/session-page/session-page.component';

const routes: Routes = [
  {
    path: "",
    component: DashboardPageComponent,
    canActivate: [AuthGuard]

  }, {
      path: ":id",
      component: SessionPageComponent,
      canActivate: [AuthGuard]

  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CoreRoutingModule { }

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SideMenuComponent } from './components/side-menu/side-menu.component';
import { MobileMenuComponent } from './components/mobile-menu/mobile-menu.component';
import { MobileNavbarComponent } from './components/mobile-navbar/mobile-navbar.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [SideMenuComponent, MobileMenuComponent, MobileNavbarComponent],
  imports: [CommonModule, RouterModule],
  exports: [SideMenuComponent, MobileMenuComponent, MobileNavbarComponent],
})
export class LayoutModule {}

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth/services/auth.service';
import { MenuService } from '../../services/menu.service';

@Component({
  selector: 'app-mobile-menu',
  templateUrl: './mobile-menu.component.html',
  styleUrls: ['./mobile-menu.component.scss'],
})
export class MobileMenuComponent implements OnInit {
  open = false;
  menu = [];
  constructor(
    private ms: MenuService,
    private as: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.menu = this.ms.get();
  }

  toggle() {
    this.open = !this.open;
  }

  signOut() {
    this.as.signout();
    this.toggle();
    this.router.navigate(['/signin']);
  }

  navigate(href) {
    this.toggle();
    this.router.navigate([href]);
  }
}

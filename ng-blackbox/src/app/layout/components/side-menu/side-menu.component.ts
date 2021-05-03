import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth/services/auth.service';
import { MenuService } from '../../services/menu.service';

@Component({
  selector: 'app-side-menu',
  templateUrl: './side-menu.component.html',
  styleUrls: ['./side-menu.component.scss'],
})
export class SideMenuComponent implements OnInit {
  menu = [];

  constructor(
    private as: AuthService,
    private ms: MenuService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.menu = this.ms.get();
  }

  isSignedIn() {
    return this.as.isSignedIn();
  }

  signOut() {
    this.as.signout();
    this.router.navigate(['/signin']);
  }
}

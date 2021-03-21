import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth/services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  constructor(private as: AuthService, private router: Router) {}

  isSignedIn() {
    return this.as.isSignedIn();
  }
  signOut() {
    this.as.signout();
    this.router.navigate(['/signin']);
  }
}

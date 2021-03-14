import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-sign-in-page',
  templateUrl: './sign-in-page.component.html',
  styleUrls: ['./sign-in-page.component.scss']
})
export class SignInPageComponent implements OnInit {

  constructor(
    private as: AuthService,
    private router: Router) { }

  ngOnInit(): void {
  }

  onSubmit(form) {
    const { username, password } = form.value;
    this.as.signin(username, password).subscribe(resp => {
      this.router.navigate(["/dashboard"]);
    })
  }
}

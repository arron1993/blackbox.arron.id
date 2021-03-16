import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { tap, shareReplay } from 'rxjs/operators';

// @ts-ignore
import jwt_decode from "jwt-decode";

import * as moment from 'moment';

interface JWTPayload {
  user_id: number;
  username: string;
  email: string;
  exp: number;
}

@Injectable({
  providedIn: 'root'
})

export class AuthService {

  private apiRoot = '/api/';

  constructor(private http: HttpClient) { }

  private setSession(authResult) {
    console.log(authResult);
    const token = authResult.access;
    const payload = <JWTPayload>jwt_decode(token);
    const expiresAt = moment.unix(payload.exp);

    localStorage.setItem('token', token);
    if (authResult.refresh !== undefined) {
      localStorage.setItem('refreshToken', authResult.refresh);
    }

    localStorage.setItem('expires_at', JSON.stringify(expiresAt.valueOf()));
  }

  get token(): string {
    return localStorage.getItem('token');
  }

  get rToken(): string {
    return localStorage.getItem('refreshToken');
  }

  signin(username: string, password: string) {
    return this.http.post(
      this.apiRoot.concat('signin/'),
      { username, password }
    ).pipe(
      tap(response => {
        this.setSession(response)
      }),
      shareReplay(),
    );
  }

  signup(email: string, password: string) {
    return this.http.post(
      this.apiRoot.concat('signup/'), {
      "username": email,
      "password": password,
    }
    ).pipe(
      tap(response => this.setSession(response)),
      shareReplay(),
    );
  }

  signout() {
    localStorage.removeItem('token');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('expires_at');
  }

  refreshToken() {
    if (moment().isBetween(this.getExpiration().subtract(1, 'days'), this.getExpiration())) {
      return this.http.post(
        this.apiRoot.concat('signin/refresh/'),
        { refresh: this.rToken }
      ).pipe(
        tap(response => this.setSession(response)),
        shareReplay(),
      ).subscribe();
    }
  }

  getExpiration() {
    const expiration = localStorage.getItem('expires_at');
    const expiresAt = JSON.parse(expiration);

    return moment(expiresAt);
  }

  isSignedIn() {
    return moment().isBefore(this.getExpiration());
  }

  isSignedOut() {
    return !this.isSignedIn();
  }

  whoami(): any {
    const jwtToken = localStorage.getItem("token");
    return jwt_decode(jwtToken);
  }
}



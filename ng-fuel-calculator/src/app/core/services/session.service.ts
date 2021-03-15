import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SessionService {

  constructor(private http: HttpClient) { }

  get() {
      return this.http.get("/api/session/")
  }

  getDetail(sessionId) {
      return this.http.get(`/api/session/${sessionId}/`)
  }
}

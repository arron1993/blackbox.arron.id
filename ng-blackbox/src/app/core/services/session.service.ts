import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class SessionService {
  constructor(private http: HttpClient) {}

  toQueryString(obj) {
    const str = [];
    for (const p in obj)
      if (obj[p] !== null && obj.hasOwnProperty(p)) {
        str.push(encodeURIComponent(p) + '=' + encodeURIComponent(obj[p]));
      }
    return str.join('&');
  }

  get(filters) {
    const queryString = this.toQueryString(filters);
    return this.http.get(`/api/session/?${queryString}`);
  }

  getDetail(sessionId) {
    return this.http.get(`/api/session/${sessionId}/`);
  }
}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class CircuitService {
  constructor(private http: HttpClient) {}

  get() {
    return this.http.get('/api/circuits/');
  }

  getDetail(id) {}
}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class MetricService {
  constructor(private http: HttpClient) {}

  getLastSession() {
    return this.http.get('/api/metrics/last-session/');
  }

  getCircuitSummary(carGroup) {
    return this.http.get(`/api/metrics/circuits/${carGroup}/`);
  }
}

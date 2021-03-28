import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class FuelService {
  constructor(private http: HttpClient) {}

  get(carID, circuitID) {
    return this.http.get(`/api/fuel/${carID}/${circuitID}`);
  }
}

import { Injectable } from '@angular/core';
import { Circuit } from '../classes/circuit';
import { Laptime } from '../classes/laptime';

@Injectable({
  providedIn: 'root'
})
export class CircuitService {
  circuits = [
    new Circuit("Circuit De Barcelona - Catalunya", new Laptime(0, 0), 2.85),
    new Circuit("Brands Hatch Circuit", new Laptime(0, 0), 2.65),
    new Circuit("Hungaroring", new Laptime(0, 0), 2.71),
    new Circuit("Misano World Circuit", new Laptime(0, 0), 2.66),
    new Circuit("Monza Circuit", new Laptime(0, 0), 3.74),
    new Circuit("Nurburgring", new Laptime(0, 0), 3.2),
    new Circuit("Paul Ricard", new Laptime(1, 59), 3.45),
    new Circuit("Silverstone", new Laptime(2, 2.850), 3.55),
    new Circuit("Circuit De Spa-Francorchamps", new Laptime(0, 0), 4.1),
    new Circuit("Circuit Zandvoort", new Laptime(0, 0), 2.66),
    new Circuit("Circuit Zolder", new Laptime(0, 0), 2.8),
    new Circuit("Kyalami Grand Prix Circuit", new Laptime(0, 0), 2.85),
    new Circuit("Suzuka Circuit", new Laptime(0, 0), 3.8),
    new Circuit("Weathertech®️ Raceway Laguna Seca", new Laptime(0, 0), 2.7),
    new Circuit("Mount Panorama Circuit", new Laptime(0, 0), 4),
    new Circuit("Autodromo Internazionale Enzo e Dino Ferrari – Imola   ", new Laptime(0, 0), 3.3),
    new Circuit("Donington Park Circuit", new Laptime(0, 0), 2.6),
    new Circuit("Oulton Park Circuit", new Laptime(0, 0), 2.45),
    new Circuit("Snetterton Circuit ", new Laptime(0, 0), 2.7),
  ]
  constructor() { }

  get() {
    return this.circuits;
  }

}

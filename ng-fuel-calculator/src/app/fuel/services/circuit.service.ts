import { Injectable } from '@angular/core';
import { Circuit } from '../classes/circuit';
import { Laptime } from '../classes/laptime';

@Injectable({
  providedIn: 'root'
})
export class CircuitService {
  circuits = [
    new Circuit("Barcelona", new Laptime(0, 0), 0),
    new Circuit("Brands Hatch", new Laptime(0, 0), 0),
    new Circuit("Hungaroring", new Laptime(0, 0), 0),
    new Circuit("Misano", new Laptime(0, 0), 0),
    new Circuit("Monza", new Laptime(0, 0), 0),
    new Circuit("Nurburgring", new Laptime(0, 0), 0),
    new Circuit("Paul Ricard", new Laptime(1, 59), 3.5),
    new Circuit("Silverstone", new Laptime(0, 0), 0),
    new Circuit("Spa-Francorchamps", new Laptime(0, 0), 0),
    new Circuit("Zandvoort", new Laptime(0, 0), 0),
    new Circuit("Zolder", new Laptime(0, 0), 0),
    new Circuit("Kyalami Grand Prix Circuit", new Laptime(0, 0), 0),
    new Circuit("Suzuka Circuit", new Laptime(0, 0), 0),
    new Circuit("Weathertech ®️ Raceway Laguna Seca", new Laptime(0, 0), 0),
    new Circuit("Mount Panorama Circuit", new Laptime(0, 0), 0),
    new Circuit("Autodromo Internazionale Enzo e Dino Ferrari – Imola   ", new Laptime(0, 0), 0),
    new Circuit("Donington Park Circuit", new Laptime(0, 0), 0),
    new Circuit("Oulton Park Circuit", new Laptime(0, 0), 0),
    new Circuit("Snetterton Circuit ", new Laptime(0, 0), 0),
  ]
  constructor() { }

  get() {
    return this.circuits;
  }

}

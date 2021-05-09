import { Injectable } from '@angular/core';
import { Split } from '../classes/split';

@Injectable({
  providedIn: 'root',
})
export class SplitService {
  constructor() {}

  circuits = [
    // RCI Classes
    new Split('barcelona', '1:44.500', '1:45.900', '1:47.900', '1:48.000'),
    new Split('bathurst', '2:02.500', '2:03.900', '2:05.900', '2:06.000'),
    new Split('brands_hatch', '1:24.000', '1:25.400', '1:26.900', '1:27.000'),
    new Split('hungaroring', '1:44.500', '1:45.900', '1:47.400', '1:47.500'),
    new Split('kyalami', '1:42.000', '1:43.400', '1:45.400', '1:45.500'),
    new Split('lagnuna_seca', '1:23.500', '1:24.900', '1:26.400', '1:26.500'),
    new Split('misano', '1:34.500', '1:35.900', '1:37.400', '1:37.500'),
    new Split('monza', '1:48.500', '1:49.900', '1:51.900', '1:52.000'),
    new Split('nurburgring', '1:55.000', '1:56.400', '1:57.900', '1:58.000'),
    new Split('paul_ricard', '1:55.000', '1:56.400', '1:58.400', '1:58.500'),
    new Split('silverstone', '1:59.500', '2:00.900', '2:02.400', '2:02.500'),
    new Split('spa', '2:19.500', '2:20.900', '2:22.900', '2:23.000'),
    new Split('suzuka', '2:01.000', '2:02.400', '2:04.400', '2:04.500'),
    new Split('zandvoort', '1:36.000', '1:37.400', '1:38.900', '1:39.000'),
    new Split('zolder', '1:29.000', '1:30.400', '1:31.900', '1:32.000'),

    // my guesses
    new Split('imola', '1:42.000', '1:43.500', '1:44.500', '1:44.600'),
    new Split('donington', '1:28.000', '1:29.000', '1:30.000', '1:30.100'),
    new Split('oulton_park', '1:34.000', '1:35.000', '1:36.000', '1:36.100'),
  ];

  get(circuit, time) {
    circuit = this.circuits.find((x) => x.circuit == circuit);
    if (circuit) {
      return circuit.getSplit(time);
    }
  }
}

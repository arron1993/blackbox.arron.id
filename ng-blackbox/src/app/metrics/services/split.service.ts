import { Injectable } from '@angular/core';
import { Split } from '../classes/split';

@Injectable({
  providedIn: 'root',
})
export class SplitService {
  constructor() {}

  circuits = [
    // RCI Classes
    new Split('barcelona', '1:44.5', '1:45.9', '1:47.9', '1:48.0'),
    new Split('bathurst', '2:02.5', '2:03.9', '2:05.9', '2:06.0'),
    new Split('brands_hatch', '1:24.0', '1:25.4', '1:26.9', '1:27.0'),
    new Split('hungaroring', '1:44.5', '1:45.9', '1:47.4', '1:47.5'),
    new Split('kyalami', '1:42.0', '1:43.4', '1:45.4', '1:45.5'),
    new Split('lagnuna_seca', '1:23.5', '1:24.9', '1:26.4', '1:26.5'),
    new Split('misano', '1:34.5', '1:35.9', '1:37.4', '1:37.5'),
    new Split('monza', '1:48.5', '1:49.9', '1:51.9', '1:52.0'),
    new Split('nurburgring', '1:55.0', '1:56.4', '1:57.9', '1:58.0'),
    new Split('paul_ricard', '1:55.0', '1:56.4', '1:58.4', '1:58.5'),
    new Split('silverstone', '1:59.5', '2:00.9', '2:02.4', '2:02.5'),
    new Split('spa', '2:19.5', '2:20.9', '2:22.9', '2:23.0'),
    new Split('suzuka', '2:01.0', '2:02.4', '2:04.4', '2:04.5'),
    new Split('zandvoort', '1:36.0', '1:37.4', '1:38.9', '1:39.0'),
    new Split('zolder', '1:29.0', '1:30.4', '1:31.9', '1:32.0'),

    // my guesses
    new Split('imola', '1:42.0', '1:43.5', '1:44.5', '1:44.6'),
    new Split('donington', '1:28.0', '1:29.0', '1:30.0', '1:30.1'),
    new Split('oulton_park', '1:34.0', '1:35.0', '1:36.0', '1:36.1'),
  ];

  get(circuit, time) {
    circuit = this.circuits.find((x) => x.circuit == circuit);
    if (circuit) {
      return circuit.getSplit(time);
    }
  }
}

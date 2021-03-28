import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class TimeService {
  constructor() {}

  convertTime(time) {
    const ms = time % 1000;
    time = (time - ms) / 1000;

    const seconds = time % 60;
    time = (time - seconds) / 60;
    const mins = time % 60;
    const minsPadded = mins.toString().padStart(2, '0');
    const secondsPadded = seconds.toString().padStart(2, '0');
    const msPadded = ms.toString().padStart(3, '0');

    return {
      minutes: minsPadded,
      seconds: secondsPadded,
      milliseconds: msPadded,
    };
  }
}

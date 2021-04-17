import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class TimeService {
  constructor() {}

  convertTime(duration) {
    let milliseconds = duration % 1000;
    let seconds = Math.floor((duration / 1000) % 60);
    let minutes = Math.floor((duration / (1000 * 60)) % 60);
    let hours = Math.floor((duration / (1000 * 60 * 60)) % 24);

    const hh = hours < 10 ? '0' + hours : hours;
    const mm = minutes < 10 ? '0' + minutes : minutes;
    const ss = seconds < 10 ? '0' + seconds : seconds;
    const ms = milliseconds < 100 ? '0' + milliseconds : milliseconds;
    return {
      hours: hh,
      minutes: mm,
      seconds: ss,
      milliseconds: ms,
    };
  }

  toMinutes(duration) {
    return duration / 1000 / 60;
  }
}

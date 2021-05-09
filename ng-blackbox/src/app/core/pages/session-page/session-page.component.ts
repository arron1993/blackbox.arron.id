import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SessionService } from '../../services/session.service';
import { TimeService } from '../../services/time.service';

@Component({
  selector: 'app-session-page',
  templateUrl: './session-page.component.html',
  styleUrls: ['./session-page.component.scss'],
})
export class SessionPageComponent implements OnInit {
  lapCount = 0;
  lapTimes = [];
  sector1Times = [];
  sector2Times = [];
  sector3Times = [];

  session = null;
  fastestLapTime = null;
  fastestSector1 = null;
  fastestSector2 = null;
  fastestSector3 = null;

  flPressures = [];
  frPressures = [];
  rlPressures = [];
  rrPressures = [];

  constructor(
    private route: ActivatedRoute,
    private ss: SessionService,
    private ts: TimeService
  ) {}

  lapCountArray() {
    const count = [];
    for (let x = 0; x < this.lapCount; x++) {
      count.push(x + 1);
    }
    return count;
  }
  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.ss.getDetail(params.id).subscribe((resp: any) => {
        this.session = resp;
        let laps = this.session.stints.map((stint) => stint.laps);
        laps = [].concat.apply([], laps);
        this.lapCount = laps.length;

        for (const lap of laps) {
          this.lapTimes.push(lap.time);
          this.sector1Times.push(lap.sector1);
          this.sector2Times.push(lap.sector2 - lap.sector1);
          this.sector3Times.push(lap.sector3 - lap.sector2);
          this.flPressures.push(lap.front_left_pressure);
          this.frPressures.push(lap.front_right_pressure);
          this.rlPressures.push(lap.rear_left_pressure);
          this.rrPressures.push(lap.rear_right_pressure);
        }

        this.fastestSector1 = Math.min(...this.sector1Times);
        this.fastestSector2 = Math.min(...this.sector2Times);
        this.fastestSector3 = Math.min(...this.sector3Times);
        this.fastestLapTime = Math.min(...this.lapTimes);
      });
    });
  }

  getRealSectorTime(lap, sector) {
    switch (sector) {
      case 1:
        return lap.sector1;
        break;
      case 2:
        return lap.sector2 - lap.sector1;

      case 3:
        return lap.sector3 - lap.sector2;
    }
  }

  get medianLaptime() {
    const median = [...this.lapTimes].sort()[
      Math.floor((this.lapTimes.length - 1) / 2)
    ];
    return this.convertTime(median);
  }

  convertTime(duration) {
    const time = this.ts.convertTime(duration);
    return `${time.minutes}:${time.seconds}:${time.milliseconds}`;
  }

  formatSessionLength(length) {
    if (length < 0) {
      return 'N/A';
    } else {
      const time = this.ts.convertTime(length);

      if (time.hours !== '00') {
        return `${time.hours} hours ${time.minutes} minutes`;
      } else {
        return `${time.minutes} minutes`;
      }
    }
  }

  formatDate(isoDate) {
    return new Date(isoDate).toISOString().substring(0, 10);
  }
}

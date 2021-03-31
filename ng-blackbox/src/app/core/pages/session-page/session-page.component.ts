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

  constructor(
    private route: ActivatedRoute,
    private ss: SessionService,
    private ts: TimeService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.ss.getDetail(params.id).subscribe((resp: any) => {
        this.session = resp;
        let fastestLapTime = null;
        let fastestSector1 = { time: null, realTime: null };
        let fastestSector2 = { time: null, realTime: null };
        let fastestSector3 = { time: null, realTime: null };
        let lapTimes = [];
        let sector1Times = [];
        let sector2Times = [];
        let sector3Times = [];
        for (let stint of this.session.stints) {
          for (let lap of stint.laps) {
            lapTimes.push(lap.time);
            let sector1 = lap.sector1;
            let sector2 = lap.sector2 - sector1;
            let sector3 = lap.sector3 - sector2;
            sector1Times.push(sector1);
            sector2Times.push(sector2);
            sector3Times.push(sector3);

            if (lap.time < fastestLapTime || fastestLapTime === null) {
              fastestLapTime = lap.time;
            }
            // probably a more efficient way of doing this
            if (
              sector1 < fastestSector1.realTime ||
              fastestSector1.realTime === null
            ) {
              fastestSector1 = { time: lap.sector1, realTime: sector1 };
            }
            if (
              sector2 < fastestSector2.realTime ||
              fastestSector2.realTime === null
            ) {
              fastestSector2 = { time: lap.sector2, realTime: sector2 };
            }
            if (
              sector3 < fastestSector3.realTime ||
              fastestSector3.realTime === null
            ) {
              fastestSector3 = { time: lap.sector3, realTime: sector3 };
            }
          }
        }
        this.fastestLapTime = fastestLapTime;
        this.fastestSector1 = fastestSector1;
        this.fastestSector2 = fastestSector2;
        this.fastestSector3 = fastestSector3;
        this.lapTimes = lapTimes;
        this.sector1Times = sector1Times;
        this.sector2Times = sector2Times;
        this.sector3Times = sector3Times;

        this.lapCount = lapTimes.length;
      });
    });
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
    const time = this.ts.convertTime(length);
    if (time.hours !== '00') {
      return `${time.hours} hours ${time.minutes} minutes`;
    } else {
      return `${time.minutes} minutes`;
    }
  }

  formatDate(isoDate) {
    return new Date(isoDate).toISOString().substring(0, 10);
  }
}

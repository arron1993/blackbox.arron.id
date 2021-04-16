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
        const laps = this.session.stints.map((stint) => stint.laps)[0];
        this.lapCount = laps.length;

        for (const lap of laps) {
          this.lapTimes.push(lap.time);
          this.sector1Times.push(lap.sector1);
          this.sector2Times.push(lap.sector2 - lap.sector1);
          this.sector3Times.push(lap.sector3 - lap.sector2);
        }
        this.fastestSector1 = Math.min(...this.sector1Times);
        this.fastestSector2 = Math.min(...this.sector2Times);
        this.fastestSector3 = Math.min(...this.sector3Times);
        this.fastestLapTime = Math.min(...this.lapTimes);
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

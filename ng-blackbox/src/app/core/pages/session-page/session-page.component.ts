import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SessionService } from '../../services/session.service';

@Component({
  selector: 'app-session-page',
  templateUrl: './session-page.component.html',
  styleUrls: ['./session-page.component.scss'],
})
export class SessionPageComponent implements OnInit {
  session = null;
  fastestLapTime = null;
  fastestSector1 = null;
  fastestSector2 = null;
  fastestSector3 = null;

  constructor(private route: ActivatedRoute, private ss: SessionService) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.ss.getDetail(params.id).subscribe((resp: any) => {
        this.session = resp;
        let fastestLapTime = null;
        let fastestSector1 = { time: null, realTime: null };
        let fastestSector2 = { time: null, realTime: null };
        let fastestSector3 = { time: null, realTime: null };

        for (let stint of this.session.stints) {
          for (let lap of stint.laps) {
            let sector1 = lap.sector1;
            let sector2 = lap.sector2 - sector1;
            let sector3 = lap.sector3 - sector2;
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
      });
    });
  }

  convertTime(time) {
    const ms = time % 1000;
    time = (time - ms) / 1000;
    const seconds = time % 60;
    time = (time - seconds) / 60;
    const mins = time % 60;
    const minsPadded = mins.toString().padStart(2, '0');
    const secondsPadded = seconds.toString().padStart(2, '0');
    const msPadded = ms.toString().padStart(3, '0');
    return `${minsPadded}:${secondsPadded}:${msPadded}`;
  }

  formatDate(isoDate) {
    return new Date(isoDate).toISOString().substring(0, 10);
  }
}

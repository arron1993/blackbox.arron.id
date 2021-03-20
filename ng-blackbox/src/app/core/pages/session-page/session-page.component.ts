import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SessionService } from '../../services/session.service';

@Component({
  selector: 'app-session-page',
  templateUrl: './session-page.component.html',
  styleUrls: ['./session-page.component.scss']
})
export class SessionPageComponent implements OnInit {
  session = null;

  constructor(
    private route: ActivatedRoute,
    private ss: SessionService) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      
      this.ss.getDetail(params.id).subscribe((resp: any) => {
        this.session = resp;
      })
    })
  }

  convertTime(time) {
    const ms = time % 1000;
    time = (time - ms) / 1000;
    const seconds = time % 60;
    time = (time - seconds) / 60;
    const mins = time % 60;
    console.log(mins)
    const minsPadded = mins.toString().padStart(2, "0")
    const secondsPadded = seconds.toString().padStart(2, "0")
    const msPadded = ms.toString().padStart(3, "0")
    return `${minsPadded}:${secondsPadded}:${msPadded}`;
  }

  formatDate(isoDate) {
     return new Date(isoDate).toISOString().substring(0, 10);
  }

}

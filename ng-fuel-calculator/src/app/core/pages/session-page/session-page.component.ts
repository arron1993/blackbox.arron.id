import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SessionService } from '../../services/session.service';

@Component({
  selector: 'app-session-page',
  templateUrl: './session-page.component.html',
  styleUrls: ['./session-page.component.scss']
})
export class SessionPageComponent implements OnInit {
  sessionId = null;
  laps = [];

  constructor(
    private route: ActivatedRoute,
    private ss: SessionService) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.sessionId = params.id;
      this.ss.getLaps(this.sessionId).subscribe((resp: any) => {
        this.laps = resp;
      })
    })
  }

}

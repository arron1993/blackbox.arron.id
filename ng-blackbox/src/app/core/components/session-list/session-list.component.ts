import { Component, OnInit } from '@angular/core';
import { SessionService } from '../../services/session.service';

@Component({
  selector: 'app-session-list',
  templateUrl: './session-list.component.html',
  styleUrls: ['./session-list.component.scss'],
})
export class SessionListComponent implements OnInit {
  sessions = [];
  constructor(private ss: SessionService) {}

  ngOnInit(): void {
    this.ss.get().subscribe((resp: any) => this.sessions = resp)
  }

  open(sessionId) {
    console.log(sessionId)
  }
}

import { Component, Input, OnInit } from '@angular/core';
import { SessionService } from '../../services/session.service';

@Component({
  selector: 'app-session-list',
  templateUrl: './session-list.component.html',
  styleUrls: ['./session-list.component.scss'],
})
export class SessionListComponent implements OnInit {
  @Input() carId = null;
  @Input() circuitId = null;
  @Input() sessionTypeId = null;
  nextPage = null;
  previousPage = null;
  page = 1;
  sessions = null;
  count = null;
  constructor(private ss: SessionService) {}

  ngOnInit(): void {}

  ngOnChanges(): void {
    this.page = 1;
    this.getSessions();
  }

  getSessions() {
    const filters = {
      car_id: this.carId !== 'null' ? this.carId : null,
      circuit_id: this.circuitId !== 'null' ? this.circuitId : null,
      session_type_id:
        this.sessionTypeId !== 'null' ? this.sessionTypeId : null,
      page: this.page,
    };

    this.ss.get(filters).subscribe((resp: any) => {
      this.sessions = resp.results;
      this.count = resp.count;
      this.nextPage = resp.next;
      this.previousPage = resp.previous;
    });
  }

  next() {
    this.page = this.nextPage;
    this.getSessions();
  }
  previous() {
    this.page = this.previousPage;
    this.getSessions();
  }
}

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

  sessions = [];
  constructor(private ss: SessionService) {}

  ngOnInit(): void {
    this.getSessions();
  }

  ngOnChanges(): void {
    this.getSessions();
  }

  getSessions() {
    const filters = {
      car_id: this.carId !== 'null' ? this.carId : null,
      circuit_id: this.circuitId !== 'null' ? this.circuitId : null,
    };
    console.log(filters);
    this.ss.get(filters).subscribe((resp: any) => (this.sessions = resp));
  }
}

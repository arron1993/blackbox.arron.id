import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { SessionTypeService } from '../../services/session-type.service';

@Component({
  selector: 'app-session-type-list',
  templateUrl: './session-type-list.component.html',
  styleUrls: ['./session-type-list.component.scss'],
})
export class SessionTypeListComponent implements OnInit {
  @Output() sessionType = new EventEmitter();
  sessionTypes = [];

  constructor(private sst: SessionTypeService) {}

  ngOnInit(): void {
    this.sst.get().subscribe((resp: any) => {
      this.sessionTypes = resp;
    });
  }

  onChange(e) {
    this.sessionType.emit(e.target.value);
  }
}

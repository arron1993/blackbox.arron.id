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
  typeId = null;

  constructor(private sst: SessionTypeService) {}

  ngOnInit(): void {
    this.sst.get().subscribe((resp: any) => {
      this.sessionTypes = resp;
      const typeId = sessionStorage.getItem('filter-typeId');
      if (typeId) {
        this.typeId = typeId;
        this.emit(typeId);
      }
    });
  }

  emit(value) {
    this.sessionType.emit(value);
  }

  onChange(e) {
    sessionStorage.setItem('filter-typeId', e.target.value);
    this.emit(e.target.value);
  }
}

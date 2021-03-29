import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-car-group-selector',
  templateUrl: './car-group-selector.component.html',
  styleUrls: ['./car-group-selector.component.scss'],
})
export class CarGroupSelectorComponent implements OnInit {
  @Output() group = new EventEmitter();

  groups = [
    { name: 'gt3', colour: 'orange' },
    { name: 'gt4', colour: 'red' },
    { name: 'cup', colour: 'yellow' },
    { name: 'st', colour: 'purple' },
  ];

  selectedGroup = 'gt3';
  constructor() {}

  ngOnInit(): void {}

  select(group) {
    this.selectedGroup = group;
    this.group.emit(group);
  }
}

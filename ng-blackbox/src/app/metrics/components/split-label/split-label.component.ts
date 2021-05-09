import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-split-label',
  templateUrl: './split-label.component.html',
  styleUrls: ['./split-label.component.scss'],
})
export class SplitLabelComponent implements OnInit {
  @Input() split;
  constructor() {}

  ngOnInit(): void {}
}

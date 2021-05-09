import { Component, Input, OnInit } from '@angular/core';
import { ChartDataSets } from 'chart.js';
import { Color, Label } from 'ng2-charts';

@Component({
  selector: 'app-generic-line-chart',
  templateUrl: './generic-line-chart.component.html',
  styleUrls: ['./generic-line-chart.component.scss'],
})
export class GenericLineChartComponent implements OnInit {
  @Input() data;
  @Input() labels;

  public _data: ChartDataSets[] = [];
  public _labels: Label[] = [];

  public options = {
    responsive: true,
    maintainAspectRatio: false,
  };

  public colours: Color[] = [];

  public legend = true;
  public chartType = 'line';

  constructor() {}

  ngOnInit(): void {
    for (let dataEntry of this.data) {
      this._data.push({
        label: dataEntry[0],
        data: dataEntry[1],
      });
    }

    this._labels = this.labels;
    let colour = Math.floor(Math.random() * 255);
    for (let i = 0; i < this._data.length; i++) {
      this.colours.push({
        backgroundColor: `hsl(${colour}, 100%, 50%)`,
      });

      // randomise the different a bit so when it wraps
      // we don't end up with the same colours
      const variance = Math.floor(Math.random() * 25);
      colour = (colour + (50 + variance)) % 255;
      console.log(colour);
    }
  }
}

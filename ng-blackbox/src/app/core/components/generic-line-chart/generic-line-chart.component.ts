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
  @Input() yCallback;
  @Input() options;

  _data: ChartDataSets[] = [];
  _labels: Label[] = [];

  _options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      yAxes: [
        {
          stacked: false,
          type: 'linear',
          ticks: {
            callback: this._yCallback,
          },
        },
      ],
      xAxes: [{ stacked: false }],
    },
  };

  colours: Color[] = [];

  legend = true;
  chartType = 'line';

  constructor() {}

  _yCallback(value) {
    return value;
  }

  setColours() {
    let colour = Math.floor(Math.random() * 255);
    for (let i = 0; i < this._data.length; i++) {
      this.colours.push({
        borderColor: `hsl(${colour}, 100%, 50%)`,
        backgroundColor: 'rgba(255,0,0,0.0)',
      });

      // randomise the different a bit so when it wraps
      // we don't end up with the same colours
      const variance = Math.floor(Math.random() * 25);
      colour = (colour + (50 + variance)) % 255;
    }
  }

  setOptions() {
    if (this.options) {
      this._options = this.options;
    }
  }

  ngOnInit(): void {
    for (let dataEntry of this.data) {
      this._data.push({
        label: dataEntry[0],
        data: dataEntry[1],
      });
    }

    this._labels = this.labels;
    this.setColours();
    this.setOptions();
  }
}

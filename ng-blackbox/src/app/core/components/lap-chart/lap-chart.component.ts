import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-lap-chart',
  templateUrl: './lap-chart.component.html',
  styleUrls: ['./lap-chart.component.scss'],
})
export class LapChartComponent implements OnInit {
  @Input() labels;
  @Input() data;

  firstLap = null;
  _data = [];
  _labels = [];

  public options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      yAxes: [
        {
          type: 'linear',
          ticks: {
            callback: (value) => {
              return this.formatTime(value);
            },
          },
        },
      ],
    },
  };

  formatTime(time) {
    const ms = time % 1000;
    time = (time - ms) / 1000;
    const seconds = time % 60;
    time = (time - seconds) / 60;
    const mins = time % 60;
    const minsPadded = mins.toString().padStart(2, '0');
    const secondsPadded = seconds.toString().padStart(2, '0');
    const msPadded = ms.toString().padStart(3, '0');
    return `${minsPadded}:${secondsPadded}:${msPadded}`;
  }

  hideFirstLap() {
    if (!this.firstLap) {
      this.firstLap = this._data[0][1][0];
      this._data[0][1].shift();
      this._labels.shift();
    } else {
      this._data[0][1].unshift(this.firstLap);
      this._labels.unshift(1);
      this.firstLap = null;
    }
  }

  constructor() {}

  ngOnInit(): void {
    this._data = this.data;
    this._labels = this.labels;
  }
}

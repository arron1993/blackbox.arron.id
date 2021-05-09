import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-lap-chart',
  templateUrl: './lap-chart.component.html',
  styleUrls: ['./lap-chart.component.scss'],
})
export class LapChartComponent implements OnInit {
  @Input() labels: number;
  @Input() data;

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

  constructor() {}

  ngOnInit(): void {}
}

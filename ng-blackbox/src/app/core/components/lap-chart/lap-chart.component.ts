import { Component, Input, OnInit } from '@angular/core';
import { ChartDataSets } from 'chart.js';
import { Color, Label } from 'ng2-charts';

@Component({
  selector: 'app-lap-chart',
  templateUrl: './lap-chart.component.html',
  styleUrls: ['./lap-chart.component.scss'],
})
export class LapChartComponent implements OnInit {
  @Input() lapCount: number;
  @Input() lapTimes: number[];

  public lineChartData: ChartDataSets[] = [];

  public lineChartLabels: Label[] = [];

  public lineChartOptions = {
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

  public lineChartColors: Color[] = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,0,0,0.0)',
    },
  ];
  public lineChartLegend = true;
  public lineChartType = 'line';

  constructor() {}

  ngOnInit(): void {
    for (let i = 1; i <= this.lapCount; i++) {
      this.lineChartLabels.push(<Label>(<unknown>i));
    }
    this.lineChartData = [{ label: 'Times', data: this.lapTimes }];
  }
}

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
  @Input() sector1Times: number[];
  @Input() sector2Times: number[];
  @Input() sector3Times: number[];

  public lineChartData: ChartDataSets[] = [
    { data: [], label: 'Time' },
    { data: [], label: 'Sector 1' },
    { data: [], label: 'Sector 2' },
    { data: [], label: 'Sector 3' },
  ];

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
    {
      borderColor: 'red',
    },
    {
      borderColor: 'green',
    },
    {
      borderColor: 'purple',
    },
  ];
  public lineChartLegend = true;
  public lineChartType = 'line';

  constructor() {}

  ngOnInit(): void {
    for (let i = 1; i <= this.lapCount; i++) {
      this.lineChartLabels.push(<Label>(<unknown>i));
    }
    this.lineChartData[0].data = this.lapTimes;
    this.lineChartData[1].data = this.sector1Times;
    this.lineChartData[2].data = this.sector2Times;
    this.lineChartData[3].data = this.sector3Times;
  }
}

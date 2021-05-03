import { Component, Input, OnInit } from '@angular/core';
import { TimeService } from 'src/app/core/services/time.service';
import { MetricService } from '../../services/metric.service';

@Component({
  selector: 'app-car-summary-list',
  templateUrl: './car-summary-list.component.html',
  styleUrls: ['./car-summary-list.component.scss'],
})
export class CarSummaryListComponent implements OnInit {
  @Input() carID;
  results: any[];
  constructor(private ts: TimeService, private ms: MetricService) {}

  ngOnInit(): void {}

  ngOnChanges() {
    this.getTimes();
  }
  getTimes() {
    this.ms.getCarSummary(this.carID).subscribe((resp: any[]) => {
      this.results = resp;
    });
  }
}

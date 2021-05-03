import { Component, OnInit } from '@angular/core';
import { TimeService } from 'src/app/core/services/time.service';
import { MetricService } from '../../services/metric.service';

@Component({
  selector: 'app-car-summary-page',
  templateUrl: './car-summary-page.component.html',
  styleUrls: ['./car-summary-page.component.scss'],
})
export class CarSummaryPageComponent implements OnInit {
  carOne;
  carTwo;

  constructor(private ms: MetricService, private ts: TimeService) {}

  ngOnInit(): void {}
}

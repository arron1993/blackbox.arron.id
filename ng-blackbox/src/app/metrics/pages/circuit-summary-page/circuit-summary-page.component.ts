import { Component, OnInit } from '@angular/core';
import { TimeService } from 'src/app/core/services/time.service';
import { MetricService } from '../../services/metric.service';

@Component({
  selector: 'app-circuit-summary-page',
  templateUrl: './circuit-summary-page.component.html',
  styleUrls: ['./circuit-summary-page.component.scss'],
})
export class CircuitSummaryPageComponent implements OnInit {
  selectedCarGroup = 'gt3';

  circuitSummary: any[] = [];
  constructor(private ms: MetricService, private ts: TimeService) {}

  ngOnInit(): void {
    this.getSummary();
  }

  getSummary() {
    this.ms
      .getCircuitSummary(this.selectedCarGroup)
      .subscribe((summary: any[]) => {
        this.circuitSummary = summary;
        this.circuitSummary.map((x) => {
          x.best_time = this.ts.convertTime(x.best_time);
          return x;
        });
      });
  }

  updateGroup(group) {
    this.selectedCarGroup = group;
    this.getSummary();
  }
}

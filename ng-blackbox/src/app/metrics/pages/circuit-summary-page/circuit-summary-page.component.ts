import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { TimeService } from 'src/app/core/services/time.service';
import { MetricService } from '../../services/metric.service';
import { SplitService } from '../../services/split.service';

@Component({
  selector: 'app-circuit-summary-page',
  templateUrl: './circuit-summary-page.component.html',
  styleUrls: ['./circuit-summary-page.component.scss'],
})
export class CircuitSummaryPageComponent implements OnInit {
  selectedCarGroup = 'gt3';
  circuitSummary: any[] = [];
  selectedCircuit;
  constructor(
    private ms: MetricService,
    private ts: TimeService,
    private ss: SplitService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.getSummary();
    this.route.fragment.subscribe((fragment: string) => {
      this.selectedCircuit = fragment;
    });
  }

  getSummary() {
    this.ms
      .getCircuitSummary(this.selectedCarGroup)
      .subscribe((summary: any[]) => {
        this.circuitSummary = summary;
        this.circuitSummary.map((x) => {
          x.split = this.ss.get(x.circuit.keyname, x.best_time);
          x.best_time = this.ts.convertTime(x.best_time);
          x.median_time = this.ts.convertTime(x.median_time);
          return x;
        });
      });
  }

  updateGroup(group) {
    this.selectedCarGroup = group;
    this.getSummary();
  }
}

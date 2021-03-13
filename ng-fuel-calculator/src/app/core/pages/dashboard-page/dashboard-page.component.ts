import { Component, OnInit } from '@angular/core';
import { CircuitService } from '../../services/circuit.service';

@Component({
  selector: 'app-dashboard-page',
  templateUrl: './dashboard-page.component.html',
  styleUrls: ['./dashboard-page.component.scss']
})
export class DashboardPageComponent implements OnInit {
  circuits: any[];

  constructor(private cs: CircuitService) { }

  ngOnInit(): void {
    this.cs.get().subscribe((resp: any) => {
      this.circuits = resp;
    })
  }

}

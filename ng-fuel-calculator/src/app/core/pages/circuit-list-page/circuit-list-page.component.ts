import { Component, OnInit } from '@angular/core';
import { CircuitService } from '../../services/circuit.service';

@Component({
  selector: 'app-circuit-list-page',
  templateUrl: './circuit-list-page.component.html',
  styleUrls: ['./circuit-list-page.component.scss']
})
export class CircuitListPageComponent implements OnInit {
  circuits: any[];

  constructor(private cs: CircuitService) { }

  ngOnInit(): void {
    this.cs.get().subscribe((resp: any) => {
      this.circuits = resp;
    })
  }

}

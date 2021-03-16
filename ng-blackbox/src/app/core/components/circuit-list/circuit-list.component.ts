import { Component, OnInit } from '@angular/core';
import { CircuitService } from '../../services/circuit.service';

@Component({
  selector: 'app-circuit-list',
  templateUrl: './circuit-list.component.html',
  styleUrls: ['./circuit-list.component.scss']
})
export class CircuitListComponent implements OnInit {

    circuits = [];
    constructor(private cs: CircuitService) { }

    ngOnInit(): void {
      this.cs.get().subscribe((resp: any) => {
        this.circuits = resp;
      })
    }

}

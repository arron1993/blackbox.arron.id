import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { CircuitService } from '../../services/circuit.service';

@Component({
  selector: 'app-circuit-list',
  templateUrl: './circuit-list.component.html',
  styleUrls: ['./circuit-list.component.scss'],
})
export class CircuitListComponent implements OnInit {
  @Output() circuit = new EventEmitter();

  circuits = [];
  constructor(private cs: CircuitService) {}

  ngOnInit(): void {
    this.cs.get().subscribe((resp: any) => {
      this.circuits = resp;
    });
  }
  onChange(event) {
    this.circuit.emit(event.target.value);
  }
}

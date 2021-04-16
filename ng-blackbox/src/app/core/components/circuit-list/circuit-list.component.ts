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
  circuitId = null;
  constructor(private cs: CircuitService) {}

  ngOnInit(): void {
    this.cs.get().subscribe((resp: any) => {
      this.circuits = resp;
      this.circuitId = sessionStorage.getItem(`filter-circuitId`);
      if (this.circuitId !== undefined) {
        this.emit(this.circuitId);
      }
    });
  }

  emit(value) {
    this.circuit.emit(value);
  }

  onChange(event) {
    const value = event.target.value;
    this.circuitId = value;
    sessionStorage.setItem(`filter-circuitId`, value);
    this.emit(value);
  }
}

import { Component, OnInit } from '@angular/core';
import { Circuit } from '../../classes/circuit';
import { CircuitService } from '../../services/circuit.service';

@Component({
  selector: 'app-calcuator',
  templateUrl: './calcuator.component.html',
  styleUrls: ['./calcuator.component.scss']
})
export class CalcuatorComponent implements OnInit {
  circuits: Circuit[] = [];
  circuit: Circuit;
  selectedCircuit;
  stintLength = 60;

  constructor(private cs: CircuitService) { }

  ngOnInit(): void {
    this.circuits = this.cs.get();
    console.log(this.circuits);
    this.selectedCircuit = this.circuits[0].name;
    this.updateCircuit(this.selectedCircuit)
    // this.circuit = this.circuits[0];
  }
  
  get fuelForStint() {
    const lapInSeconds = (this.circuit.laptime.minutes * 60) + this.circuit.laptime.seconds
    const estimatedLaps = (this.stintLength * 60) / lapInSeconds;
    const stintFuelUsage = this.circuit.fuelPerLap * estimatedLaps
    return Math.round(stintFuelUsage * 100) / 100 
  }

  updateCircuit(e) {
    this.circuit = this.circuits.find(circuit => circuit.name.trim() == e.trim())
  }
}

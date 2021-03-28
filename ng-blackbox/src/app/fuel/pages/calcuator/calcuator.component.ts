import { Component, OnInit } from '@angular/core';
import { forkJoin } from 'rxjs';
import { CarService } from 'src/app/core/services/car.service';
import { CircuitService } from 'src/app/core/services/circuit.service';
import { TimeService } from 'src/app/core/services/time.service';
import { MetricService } from 'src/app/metrics/services/metric.service';
import { FuelService } from '../../services/fuel.service';

@Component({
  selector: 'app-calcuator',
  templateUrl: './calcuator.component.html',
  styleUrls: ['./calcuator.component.scss'],
})
export class CalcuatorComponent implements OnInit {
  circuits: any[];
  cars: any[];

  selectedCar;
  selectedCircuit;
  stintLength = 30;
  lapTime = {
    minutes: '0',
    seconds: '0',
    milliseconds: '0',
  };
  fuelUsage = 0;

  constructor(
    private circuitService: CircuitService,
    private carService: CarService,
    private fs: FuelService,
    private ts: TimeService,
    private ms: MetricService
  ) {}

  ngOnInit(): void {
    let circuitCall = this.circuitService.get();
    let carCall = this.carService.get();

    forkJoin([circuitCall, carCall]).subscribe((resp: any[]) => {
      this.circuits = resp[0];
      this.cars = resp[1];
      this.ms.getLastSession().subscribe((lastSession: any) => {
        this.selectedCircuit = lastSession.circuit.id;
        this.selectedCar = lastSession.car.id;
        this.update();
      });
    });
  }

  get fuelForStint() {
    const minutes = parseInt(this.lapTime.minutes);
    const seconds = parseInt(this.lapTime.seconds);
    const milliseconds = parseInt(this.lapTime.milliseconds);
    const lapInSeconds = minutes * 60 + seconds + milliseconds / 1000;

    const estimatedLaps = (this.stintLength * 60) / lapInSeconds;
    const stintFuelUsage = this.fuelUsage * estimatedLaps;
    return Math.round(stintFuelUsage * 100) / 100;
  }

  update() {
    console.log(this.selectedCar, this.selectedCircuit);
    this.fs
      .get(this.selectedCar, this.selectedCircuit)
      .subscribe((resp: any) => {
        this.fuelUsage = resp.median_fuel_usage || this.fuelUsage;
        if (resp.median_lap_time) {
          this.lapTime = this.ts.convertTime(resp.median_lap_time);
        }
      });
  }
}

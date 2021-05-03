import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { CarService } from '../../services/car.service';

@Component({
  selector: 'app-car-list',
  templateUrl: './car-list.component.html',
  styleUrls: ['./car-list.component.scss'],
})
export class CarListComponent implements OnInit {
  @Output() car = new EventEmitter();
  @Input() filterPrefix = '';

  cars = [];
  carId = null;

  constructor(private cs: CarService) {}

  ngOnInit(): void {
    this.cs.get().subscribe((resp: any[]) => {
      this.cars = resp;
      const carId = sessionStorage.getItem(`filter-${this.filterPrefix}-carId`);
      if (carId) {
        this.carId = carId;
        this.emit(this.carId);
      }
    });
  }

  emit(value) {
    this.car.emit(value);
  }

  onChange(event) {
    const value = event.target.value;
    sessionStorage.setItem('filter-carId', value);
    this.emit(value);
  }
}

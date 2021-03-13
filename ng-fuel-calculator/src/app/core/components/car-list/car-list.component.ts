import { Component, OnInit } from '@angular/core';
import { CarService } from '../../services/car.service';

@Component({
  selector: 'app-car-list',
  templateUrl: './car-list.component.html',
  styleUrls: ['./car-list.component.scss']
})
export class CarListComponent implements OnInit {
  cars = [];

  constructor(private cs: CarService) { }

  ngOnInit(): void {
    this.cs.get().subscribe((resp: any[]) => {
      this.cars = resp
    })
  }

}

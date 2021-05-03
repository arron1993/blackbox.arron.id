import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class MenuService {
  menu = [
    {
      href: '/sessions',
      icon: 'home',
      text: 'Home',
    },
    {
      href: '/fuel',
      icon: 'local_gas_station',
      text: 'Fuel Calculator',
    },
    {
      href: '/metrics',
      icon: 'leaderboard',
      text: 'Stats',
    },
  ];
  constructor() {}

  get() {
    return this.menu;
  }
}

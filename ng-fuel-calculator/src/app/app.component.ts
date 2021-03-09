import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'ng-fuel-calculator';
  estimatedFuelUsage = 2.8;
  estimatedLapTime = {
    minutes: 1,
    seconds: 45
  }
  stintLength = 60;

  get fuelForStint() {
    const lapInSeconds = (this.estimatedLapTime.minutes * 60) + this.estimatedLapTime.seconds
    const estimatedLaps = (this.stintLength * 60) / lapInSeconds;
    const stintFuelUsage = this.estimatedFuelUsage * estimatedLaps
    return Math.round(stintFuelUsage * 100) / 100 
    
  }
}

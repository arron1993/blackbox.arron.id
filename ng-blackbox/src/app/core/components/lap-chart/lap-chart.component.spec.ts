import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LapChartComponent } from './lap-chart.component';

describe('LapChartComponent', () => {
  let component: LapChartComponent;
  let fixture: ComponentFixture<LapChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LapChartComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LapChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

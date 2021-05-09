import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GenericLineChartComponent } from './generic-line-chart.component';

describe('GenericLineChartComponent', () => {
  let component: GenericLineChartComponent;
  let fixture: ComponentFixture<GenericLineChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GenericLineChartComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GenericLineChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

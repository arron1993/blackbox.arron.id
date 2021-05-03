import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarSummaryPageComponent } from './car-summary-page.component';

describe('CarSummaryPageComponent', () => {
  let component: CarSummaryPageComponent;
  let fixture: ComponentFixture<CarSummaryPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarSummaryPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CarSummaryPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

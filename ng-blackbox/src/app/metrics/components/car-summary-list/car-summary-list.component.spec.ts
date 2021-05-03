import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarSummaryListComponent } from './car-summary-list.component';

describe('CarSummaryListComponent', () => {
  let component: CarSummaryListComponent;
  let fixture: ComponentFixture<CarSummaryListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarSummaryListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CarSummaryListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

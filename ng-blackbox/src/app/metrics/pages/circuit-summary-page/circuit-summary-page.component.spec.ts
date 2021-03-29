import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CircuitSummaryPageComponent } from './circuit-summary-page.component';

describe('CircuitSummaryPageComponent', () => {
  let component: CircuitSummaryPageComponent;
  let fixture: ComponentFixture<CircuitSummaryPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CircuitSummaryPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CircuitSummaryPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

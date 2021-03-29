import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MetricDashboardPageComponent } from './metric-dashboard-page.component';

describe('MetricDashboardPageComponent', () => {
  let component: MetricDashboardPageComponent;
  let fixture: ComponentFixture<MetricDashboardPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MetricDashboardPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MetricDashboardPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

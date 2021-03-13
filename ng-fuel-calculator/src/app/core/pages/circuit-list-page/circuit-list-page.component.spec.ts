import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CircuitListPageComponent } from './circuit-list-page.component';

describe('CircuitListPageComponent', () => {
  let component: CircuitListPageComponent;
  let fixture: ComponentFixture<CircuitListPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CircuitListPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CircuitListPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CalculatorFieldComponent } from './calculator-field.component';

describe('CalculatorFieldComponent', () => {
  let component: CalculatorFieldComponent;
  let fixture: ComponentFixture<CalculatorFieldComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CalculatorFieldComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CalculatorFieldComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

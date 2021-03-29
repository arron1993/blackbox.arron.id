import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarGroupSelectorComponent } from './car-group-selector.component';

describe('CarGroupSelectorComponent', () => {
  let component: CarGroupSelectorComponent;
  let fixture: ComponentFixture<CarGroupSelectorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarGroupSelectorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CarGroupSelectorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

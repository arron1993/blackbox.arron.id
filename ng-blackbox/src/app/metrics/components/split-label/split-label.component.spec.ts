import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SplitLabelComponent } from './split-label.component';

describe('SplitLabelComponent', () => {
  let component: SplitLabelComponent;
  let fixture: ComponentFixture<SplitLabelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SplitLabelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SplitLabelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

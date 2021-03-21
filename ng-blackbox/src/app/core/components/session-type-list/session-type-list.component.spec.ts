import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SessionTypeListComponent } from './session-type-list.component';

describe('SessionTypeListComponent', () => {
  let component: SessionTypeListComponent;
  let fixture: ComponentFixture<SessionTypeListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SessionTypeListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SessionTypeListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

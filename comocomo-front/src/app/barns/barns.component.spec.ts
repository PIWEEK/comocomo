import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BarnsComponent } from './barns.component';

describe('BarnsComponent', () => {
  let component: BarnsComponent;
  let fixture: ComponentFixture<BarnsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BarnsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BarnsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

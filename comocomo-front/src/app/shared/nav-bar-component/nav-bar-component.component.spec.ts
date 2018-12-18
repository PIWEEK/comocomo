import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NavBarComponentComponent } from './nav-bar-component.component';

describe('NavBarComponentComponent', () => {
  let component: NavBarComponentComponent;
  let fixture: ComponentFixture<NavBarComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NavBarComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NavBarComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

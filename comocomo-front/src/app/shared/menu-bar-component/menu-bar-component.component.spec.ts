import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuBarComponentComponent } from './menu-bar-component.component';

describe('MenuBarComponentComponent', () => {
  let component: MenuBarComponentComponent;
  let fixture: ComponentFixture<MenuBarComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MenuBarComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MenuBarComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

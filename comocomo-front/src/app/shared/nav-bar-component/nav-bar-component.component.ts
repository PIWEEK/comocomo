import { Component, Input } from '@angular/core';

@Component({
  selector: 'nav-bar-component',
  templateUrl: './nav-bar-component.component.html',
  styleUrls: ['./nav-bar-component.component.less']
})
export class NavBarComponentComponent {

  @Input() currentSection: string;

  constructor() { }

}

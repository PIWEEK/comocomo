import { Component, Input } from '@angular/core';

@Component({
  selector: 'menu-bar-component',
  templateUrl: './menu-bar-component.component.html',
  styleUrls: ['./menu-bar-component.component.less']
})
export class MenuBarComponentComponent {

  @Input() currentSection: string;

  constructor() { }

}

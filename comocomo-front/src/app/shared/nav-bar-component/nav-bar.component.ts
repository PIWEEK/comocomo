import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.less']
})
export class NavBarComponent {

  @Input() public content: string = '';
  @Input() public leftRouterLink: Object[] = null;
  @Input() public leftQueryParams: Object = null;
  @Input() public rightRouterLink: Object[] = null;
  @Input() public rightQueryParams: Object = null;

}

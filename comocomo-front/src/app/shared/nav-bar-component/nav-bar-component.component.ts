import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'nav-bar-component',
  templateUrl: './nav-bar-component.component.html',
  styleUrls: ['./nav-bar-component.component.less']
})
export class NavBarComponentComponent {

  @Input() public content: string = '';
  @Input() public hasLeft: boolean = true;
  @Input() public hasRight: boolean = true;
  @Output() public leftClicked = new EventEmitter<void>();
  @Output() public rightClicked = new EventEmitter<void>();

  constructor() { }

  public leftClick() {
    this.leftClicked.emit();
  }

  public rightClick() {
    this.rightClicked.emit();
  }
}

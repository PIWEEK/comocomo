import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-day',
  templateUrl: './day.component.html',
  styleUrls: ['./day.component.less']
})
export class DayComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  public slotClick(slotNumber: number) {
    console.log('slot', slotNumber);
  }

}

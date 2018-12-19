import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-week',
  templateUrl: './week.component.html',
  styleUrls: ['./week.component.less']
})
export class WeekComponent implements OnInit {

  constructor(
    private router: Router
  ) { }

  ngOnInit() {
  }

  public slotClick(slotNumber: number) {
    this.router.navigate(['/day', slotNumber]);
  }

}

import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-barns',
  templateUrl: './barns.component.html',
  styleUrls: ['./barns.component.less']
})
export class BarnsComponent implements OnInit {
  public weekStatistics$: any;

  constructor(
  ) { }

  ngOnInit() {
  }

}

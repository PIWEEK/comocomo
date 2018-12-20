import { Component, OnInit } from '@angular/core';
import { WeekStatisticsApiService } from '../data-model/week-statistics/week-statistics-api.service';

@Component({
  selector: 'app-barns',
  templateUrl: './barns.component.html',
  styleUrls: ['./barns.component.less']
})
export class BarnsComponent implements OnInit {
  public weekStatistics$: any;

  constructor(
    private statisticsService: WeekStatisticsApiService
  ) { }

  ngOnInit() {
    this.weekStatistics$ = this.statisticsService.getWeekStatistics();
    this.weekStatistics$.subscribe();
  }
}

import { Observable, zip } from 'rxjs';
import { share, filter, reduce, map } from 'rxjs/operators';
import { Component, OnInit } from '@angular/core';
import { WeekStatisticsApiService } from '../data-model/week-statistics/week-statistics-api.service';
import { WeekStatistics } from '../data-model/week-statistics/week-statistics.model';

@Component({
  selector: 'app-barns',
  templateUrl: './barns.component.html',
  styleUrls: ['./barns.component.less']
})
export class BarnsComponent implements OnInit {
  public weekStatistics$: Observable<WeekStatistics>;

  public categoryA$: Observable<number>;
  public categoryB$: Observable<number>;
  public categoryC$: Observable<number>;
  public categoryD$: Observable<number>;
  public categoryE$: Observable<number>;
  public single$: Observable<Object>;

  public multi: any[];
  public view: any[] = [300, 200];

  // options
  public showXAxis = true;
  public showYAxis = true;
  public gradient = false;
  public showLegend = false;
  public showXAxisLabel = true;
  public xAxisLabel = 'NUTRISCORE';
  public showYAxisLabel = true;
  public yAxisLabel = 'Numero de comidas';
  public colorScheme = {
    domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA']
  };

  constructor(
    private statisticsService: WeekStatisticsApiService
  ) { }

  ngOnInit() {
    this.weekStatistics$ = this.statisticsService
      .getWeekStatistics()
      .pipe(share());

    this.categoryA$ = this.weekStatistics$.pipe(
      map((foodTypes) => foodTypes.filter((food) => food.nutriscore === 'A').length)
    );

    this.categoryB$ = this.weekStatistics$.pipe(
      map((foodTypes) => foodTypes.filter((food) => food.nutriscore === 'B').length)
    );

    this.categoryC$ = this.weekStatistics$.pipe(
      map((foodTypes) => foodTypes.filter((food) => food.nutriscore === 'C').length)
    );

    this.categoryD$ = this.weekStatistics$.pipe(
      map((foodTypes) => foodTypes.filter((food) => food.nutriscore === 'D').length)
    );

    this.categoryE$ = this.weekStatistics$.pipe(
      map((foodTypes) => foodTypes.filter((food) => food.nutriscore === 'E').length)
    );

    this.single$ = zip(
      this.categoryA$,
      this.categoryB$,
      this.categoryC$,
      this.categoryD$,
      this.categoryE$,
    ).pipe(
      map(([a, b, c, d, e]) => [
        {'name': 'A', 'value': a},
        {'name': 'B', 'value': b},
        {'name': 'C', 'value': c},
        {'name': 'D', 'value': d},
        {'name': 'E', 'value': e}
      ])
    )

    this.weekStatistics$.subscribe();
  }
}

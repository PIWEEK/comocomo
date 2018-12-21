import { Observable, zip } from 'rxjs';
import { share, reduce, map, tap } from 'rxjs/operators';
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
  public showScoreDetail: boolean;
  public scoreDetailLetter: string;
  public scoreDetailedList$: Observable<Object>;

  public multi: any[];

  // options
  public showXAxis = true;
  public showYAxis = false;
  public gradient = false;
  public showLegend = false;
  public showXAxisLabel = true;
  public xAxisLabel = 'NUTRISCORE';
  public showYAxisLabel = true;
  public yAxisLabel = 'Numero de comidas';
  public colorScheme = {
    domain: [
      '#2e8141',
      '#85bb2f',
      '#f8cb06',
      '#ee8101',
      '#e63e10'
    ]
  };

  constructor(
    private statisticsService: WeekStatisticsApiService
  ) { }

  ngOnInit() {
    const filterBy = (score) => {
      return (foodTypes) => foodTypes.filter((food) => food.nutriscore === score).length
    }

    this.weekStatistics$ = this.statisticsService
      .getWeekStatistics()
      .pipe(share());

    this.categoryA$ = this.weekStatistics$.pipe(map(filterBy('A')));
    this.categoryB$ = this.weekStatistics$.pipe(map(filterBy('B')));
    this.categoryC$ = this.weekStatistics$.pipe(map(filterBy('C')));
    this.categoryD$ = this.weekStatistics$.pipe(map(filterBy('D')));
    this.categoryE$ = this.weekStatistics$.pipe(map(filterBy('E')));

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

  public onSelect(event){
    this.showScoreDetail = true;
    this.scoreDetailLetter = event.name

    const filterByScore = (score) => {
      return (foodTypes) => foodTypes.filter((food) => food.nutriscore === score)
    }

    this.scoreDetailedList$ = this
      .weekStatistics$
      .pipe(map(filterByScore(event.name)))
  }
}

import { Injectable } from '@angular/core';
import * as moment from 'moment';
import { Moment } from 'moment';

@Injectable({
  providedIn: 'root'
})
export class DatesService {

  constructor() {
    moment.locale('es-es');
  }

  public fromLink(dateString: string): Moment {
    const date = moment(dateString, 'YYYY-MM-DD');
    return date.isValid() ? date : null;
  }

  public toLink(date: Moment): string {
    return date.format('YYYY-MM-DD');
  }

  public currentWeek(): Moment {
    return moment().clone().startOf('week');
  }

  public previousWeek(date: Moment): Moment {
    return date.clone().subtract(1, 'week');
  }

  public nextWeek(date: Moment): Moment {
    return date.clone().add(1, 'week');
  }

  public weekName(week: Moment): string {
    const start = week.clone();
    const startDay = start.format('D');
    const startMonth = start.format('MMM').replace('.', '');
    const startYear = start.format('YYYY');

    const end = start.clone().add(6, 'days');
    const endDay = end.format('D');
    const endMonth = end.format('MMM').replace('.', '');
    const endYear = end.format('YYYY');

    if (startYear !== endYear) {
      return `${startDay} ${startMonth} ${startYear} - ${endDay} ${endMonth} ${endYear}`;
    }
    if (startMonth !== endMonth) {
      return `${startDay} ${startMonth} - ${endDay} ${endMonth} ${endYear}`;
    }
    return `${startDay}-${endDay} ${endMonth} ${endYear}`;
  }

  public dayName(date: Moment): string {
    return date.format('dddd D MMM').replace('.', '');
  }

  public dayNameShort(date: Moment): string {
    return date.format('dddd D');
  }

  public weekDays(): number[] {
    return Array.from(Array(7).keys());
  }

  public currentDayIndex(): number {
    return moment().weekday();
  }

  public weekDay(week: Moment, dayIndex: number) {
    return week.clone().add(dayIndex, 'days');
  }
}

import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { DatesService } from '../shared/dates-service/dates.service';
import { Moment } from 'moment';

@Component({
  selector: 'app-week',
  templateUrl: './week.component.html',
  styleUrls: ['./week.component.less'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class WeekComponent implements OnInit {

  public currentWeek: Moment;
  public currentDayIndex: number;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private dates: DatesService
  ) { }

  ngOnInit() {
    this.route.queryParamMap.subscribe(
      (params) => {
        const weekParam = params.get('week');
        if (!weekParam) {
          this.currentWeek = this.dates.currentWeek();
        } else {
          this.currentWeek = this.dates.fromLink(weekParam);
          console.log('dddd', this.currentWeek);
        }

        const openParam = params.get('open');
        if (!openParam) {
          this.currentDayIndex = null;
        } else if (openParam === 'today') {
          this.currentDayIndex = this.dates.currentDayIndex();
        } else {
          const open = parseInt(openParam, 10);
          this.currentDayIndex = isNaN(open) ? null : open;
        }
      }
    );
  }

  get currentWeekName() {
    if (this.currentWeek) {
      return this.dates.weekName(this.currentWeek);
    } else {
      return '';
    }
  }

  get currentWeekLink() {
    if (this.currentWeek) {
      return this.dates.toLink(this.currentWeek);
    } else {
      return '';
    }
  }

  get previousWeekLink() {
    if (this.currentWeek) {
      const previousWeek = this.dates.previousWeek(this.currentWeek);
      return this.dates.toLink(previousWeek);
    } else {
      return null;
    }
  }

  get nextWeekLink() {
    if (this.currentWeek) {
      const nextWeek = this.dates.nextWeek(this.currentWeek);
      return this.dates.toLink(nextWeek);
    } else {
      return null;
    }
  }

  get weekDays() {
    return this.dates.weekDays();
  }

  public weekDayName(dayIndex: number) {
    if (this.currentWeek) {
      return this.dates.weekDayName(this.currentWeek, dayIndex);
    } else {
      return 0;
    }
  }

  public slotClick(slotNumber: number) {
    this.router.navigate(['/day', slotNumber]);
  }

}

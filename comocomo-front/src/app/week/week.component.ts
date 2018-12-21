import { Component, OnInit, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Moment } from 'moment';
import { DatesService } from '../shared/dates-service/dates.service';
import { FoodRegistrationsApiService } from '../data-model/food-registrations/food-registrations-api.service';
import { FoodRegistration } from '../data-model/food-registrations/food-registrations.model';

@Component({
  selector: 'app-week',
  templateUrl: './week.component.html',
  styleUrls: ['./week.component.less'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class WeekComponent implements OnInit {

  public currentWeek: Moment;
  public currentDayIndex: number;
  public isToday: boolean;
  public savedParams = {};

  public registrations: FoodRegistration[] = [];

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private cd: ChangeDetectorRef,
    private dates: DatesService,
    private foodRegistrationsApiService: FoodRegistrationsApiService
  ) { }

  ngOnInit() {
    this.route.queryParamMap.subscribe(
      (params) => {
        const weekParam = params.get('week');
        if (!weekParam) {
          this.currentWeek = this.dates.currentWeek();
        } else {
          this.currentWeek = this.dates.fromLink(weekParam);
        }

        this.isToday = false;
        const openParam = params.get('open');
        if (!openParam) {
          this.currentDayIndex = null;
        } else if (openParam === 'today') {
          this.currentDayIndex = this.dates.currentDayIndex();
          this.isToday = true;
        } else {
          const open = parseInt(openParam, 10);
          this.currentDayIndex = isNaN(open) ? null : open;
        }

        this.savedParams = {week: weekParam, open: openParam};

        if (this.currentDayIndex) {
          this.foodRegistrationsApiService.getFoodRegistrations(
            this.dates.weekDay(this.currentWeek, this.currentDayIndex),
            this.dates.weekDay(this.currentWeek, this.currentDayIndex)
          ).subscribe(
            (registrations) => {
              this.registrations = registrations;
              this.cd.markForCheck();
            }
          )
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

  get daySlots() {
    // TODO: esto debería venir de un servicio del API de back
    return [
      'Desayuno',
      'Media mañana',
      'Comida',
      'Merienda',
      'Cena'
    ];
  }

  public weekDayName(dayIndex: number) {
    if (this.currentWeek) {
      const weekDay = this.dates.weekDay(this.currentWeek, dayIndex);
      return this.dates.dayName(weekDay);
    } else {
      return '';
    }
  }

  public weekDayLink(dayIndex: number) {
    if (this.currentWeek) {
      const weekDay = this.dates.weekDay(this.currentWeek, dayIndex);
      return this.dates.toLink(weekDay);
    } else {
      return '';
    }
  }

  public hasSlotRegistrations(slot: number) {
    return (!!this.registrations.find((it) => it.slot === slot));
  }

}

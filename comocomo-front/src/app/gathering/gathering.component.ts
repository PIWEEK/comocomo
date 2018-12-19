import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { DatesService } from '../shared/dates-service/dates.service';
import { Moment } from 'moment';
import { FoodKindsApiService } from '../data-model/food-kinds/food-kinds-api.service';

@Component({
  selector: 'app-gathering',
  templateUrl: './gathering.component.html',
  styleUrls: ['./gathering.component.less']
})
export class GatheringComponent implements OnInit {
  public errorMessage = '';
  public foodKinds$: any;

  public currentDate: Moment;
  public currentSlot: number;

  public returnParams: Object;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private dates: DatesService,
    private foodKindsApiService: FoodKindsApiService
  ) { }

  ngOnInit() {
    this.route.paramMap.subscribe(
      (params) => {
        const dateParam = params.get('date');
        this.currentDate = this.dates.fromLink(dateParam);

        const slotParam = params.get('slot');
        const slot = parseInt(slotParam, 10);
        this.currentSlot = isNaN(slot) ? null : slot;
      }
    );

    this.route.queryParamMap.subscribe(
      (params) => {
        this.returnParams = {
          week: params.get('week'),
          open: params.get('open')
        };
      }
    );

    this.foodKinds$ = this.foodKindsApiService.getFoodKinds();
    this.foodKinds$.subscribe();
  }

  get slotName() {
    // TODO: esto debería venir de un servicio del API de back
    const daySlots = [
      'desayunado',
      'comido a media mañana',
      'comido',
      'merendado',
      'cenado'
    ];
    return daySlots[this.currentSlot] || '';
  }

  get dayNameShort() {
    if (this.currentDate) {
      return this.dates.dayNameShort(this.currentDate);
    } else {
      return '';
    }
  }
}

import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { withLatestFrom } from 'rxjs/operators';
import { FoodKind } from '../data-model/food-kinds/food-kinds.model';
import { FoodTypesApiService } from '../data-model/food-types/food-types-api.service';
import { FoodType } from '../data-model/food-types/food-types.model';

@Component({
  selector: 'food-type',
  templateUrl: './food-type.component.html',
  styleUrls: ['./food-type.component.less']
})
export class FoodTypeComponent implements OnInit {

  @Input() foodKind: FoodKind;
  @Input() foodType: FoodType;
  @Output() public changed: EventEmitter<FoodType> = new EventEmitter();

  public foodTypes$: Observable<FoodType[]>;
  private inputChanged$ = new Subject<string>();

  constructor(
    private foodTypesApiService: FoodTypesApiService
  ) { }

  ngOnInit() {
    this.foodTypes$ = this.foodTypesApiService.getFoodTypes(this.foodKind.id);

    this.inputChanged$
      .pipe(withLatestFrom(this.foodTypes$))
      .subscribe(([value, foodTypes]) => {
        const foodType = foodTypes.find((it) => it.name === value);
        if (foodType) {
          this.changed.emit(foodType);
        }
      });
  }

  public inputChanged(evt: any) {
    this.inputChanged$.next(evt.target.value);
  }
}

import { Component, OnInit, Input } from '@angular/core';
import { Observable } from 'rxjs';
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
  public foodTypes$: Observable<FoodType[]>;

  constructor(
    private foodTypesApiService: FoodTypesApiService
  ) { }

  ngOnInit() {
    this.foodTypes$ = this.foodTypesApiService.getFoodTypes(this.foodKind.id);
  }
}

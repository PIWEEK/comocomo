import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FoodKindsApiService } from '../data-model/food-kinds/food-kinds-api.service';

@Component({
  selector: 'app-gathering',
  templateUrl: './gathering.component.html',
  styleUrls: ['./gathering.component.less']
})
export class GatheringComponent implements OnInit {
  public errorMessage = '';
  public foodKinds$: any;

  constructor(
    private router: Router,
    private foodKindsApiService: FoodKindsApiService
  ) { }


  ngOnInit() {
    this.foodKinds$ = this.foodKindsApiService.getFoodKinds();
    this.foodKinds$.subscribe();
  }
}

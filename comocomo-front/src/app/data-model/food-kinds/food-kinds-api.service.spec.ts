import { TestBed } from '@angular/core/testing';

import { FoodKindsApiService } from './food-kinds-api.service';

describe('FoodKindsApiService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: FoodKindsApiService = TestBed.get(FoodKindsApiService);
    expect(service).toBeTruthy();
  });
});

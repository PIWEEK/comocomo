import { TestBed } from '@angular/core/testing';

import { DatesServiceService } from './dates-service.service';

describe('DatesServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: DatesServiceService = TestBed.get(DatesServiceService);
    expect(service).toBeTruthy();
  });
});

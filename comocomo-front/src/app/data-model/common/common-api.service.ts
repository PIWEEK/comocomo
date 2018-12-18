import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class CommonApiService {
  constructor() {}

  public getApiUrl(slug: string = null): string {
    const url = `http://localhost:8000/api/v1${slug}/`;
    return url;
  }
}

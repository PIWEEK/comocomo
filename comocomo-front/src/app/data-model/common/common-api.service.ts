import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class CommonApiService {
  constructor() {}

  public getApiUrl(slug: string = null): string {
    const url = `http://10.8.1.111:8000/api/v1${slug}/`;
    return url;
  }
}

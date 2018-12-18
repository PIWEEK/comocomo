import { Injectable } from '@angular/core';
import { of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersApiService {

  constructor() { }

  public login(username: string, password: string) {
    return of('success');
  }
}

import { catchError } from 'rxjs/internal/operators';
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { CommonApiService } from '../common/common-api.service';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersApiService {

  constructor(
    private http: HttpClient,
    private apiService: CommonApiService
    ) { }

  public login(username: string, password: string) {
    const url = this.apiService.getApiUrl('/login');
    return this.http.post(url, {username, password}).pipe(
      catchError(this.handleError)
    );
  }

  private handleError(error: HttpErrorResponse) {
    let userMessage = 'Something bad happened; please try again later.';

    if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
      if (error.error.non_field_errors) {
        userMessage = error.error.non_field_errors[0];
      }
    }
    // return an observable with a user-facing error message
    return throwError(userMessage);
  }
}

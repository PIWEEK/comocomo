import { catchError } from 'rxjs/internal/operators';
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { CommonApiService } from '../common/common-api.service';
import { throwError } from 'rxjs';
import { DatesService } from '../../shared/dates-service/dates.service';
import { HttpHeaders } from '@angular/common/http';
import { WeekStatistics } from './week-statistics.model';

@Injectable({
  providedIn: 'root'
})
export class WeekStatisticsApiService {

  constructor(
    private http: HttpClient,
    private apiService: CommonApiService,
    private dates: DatesService
  ) { }

  public getWeekStatistics() {
    const toDate = this.dates.today();
    const fromDate = this.dates.previousWeek(toDate);
    const link = `/week-statistics/${this.dates.toLink(fromDate)}/${this.dates.toLink(toDate)}`;
    const url = this.apiService.getApiUrl(link);
    const httpOptions =  {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Authorization': '3553959c9fa6f8d90174d07dfc31f2d1eb147492'
      })
    }

    return this.http.get<WeekStatistics>(url, httpOptions);
  }
}

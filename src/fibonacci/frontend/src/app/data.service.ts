import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';

import { ErrorObservable } from 'rxjs/observable/ErrorObservable';
import { catchError, retry } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { InputNumber } from './home/input';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable()
export class DataService {

  dataUrl = 'api/fibonacci-viewset/';
  constructor(private http: HttpClient) { }


  getData() {
    return this.http.get(this.dataUrl)
    .pipe(catchError(this.handleError));
  }

  getFibonacciNum(num: InputNumber): Observable<InputNumber>{
    return this.http.post<InputNumber>(this.dataUrl, num, httpOptions);
            // .pipe(catchError(this.handleError));
  }

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error('An error occurred:', error.error.message);
    } else {
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    return new ErrorObservable(
      'Something bad happened; please try again later.');
  };
}

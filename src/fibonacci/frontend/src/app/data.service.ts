import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
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
    return this.http.get(this.dataUrl);
  }

  getFibonacciNum(num: InputNumber): Observable<InputNumber>{
    return this.http.post<InputNumber>(this.dataUrl, num, httpOptions);
  }
}

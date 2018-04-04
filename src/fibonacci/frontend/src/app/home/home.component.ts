import { Component, OnInit } from '@angular/core';

import { DataService } from '../data.service';
import { InputNumber } from './input';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  
  fibonacciNumber: number = 4;
  inputNumber: number = 0;
  history = [];
  itemCount: number = 0; 
  result = undefined;
  num: number;
  fibonacciResult: string = "";
  timeTaken:any = undefined;
  constructor(private _data: DataService) { }

  ngOnInit() {
    this.fibonacciNumber = 0;
    this.inputNumber = 0;
    this.fibonacciResult ="";
    this.itemCount = this.history.length;
    this.result = undefined;
    this.showData();
  }

  
  GetFibonacciNumber(input_number: number, fibonacci_result: string): void{
    var t0: any = performance.now();
    var t1: any = undefined;
    const num1: InputNumber = {input_number, fibonacci_result} as InputNumber;
    this._data.getFibonacciNum(num1).subscribe(
      res=>{
        this.fibonacciResult = res.fibonacci_result;
        t1 = performance.now();
        this.timeTaken = t1-t0;
      }
    );
  }

  showData(){
    this._data.getData().subscribe(data=>{
      this.result = data;
      console.log(this.result);
      this.itemCount = this.result.length;
    });
    
  }

}

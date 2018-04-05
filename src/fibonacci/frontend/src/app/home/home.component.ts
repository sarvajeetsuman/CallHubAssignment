import { Component, OnInit } from '@angular/core';


import { DataService } from '../data.service';
import { InputNumber } from './input';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  
  inputNumber: number = 0;
  history = [];
  itemCount: number = 0; 
  result = undefined;
  num: number;
  fibonacciResult: string = "";
  timeTaken:any = 0;
  flag: boolean = false;

  f = undefined;
  constructor(private _data: DataService) { }

  ngOnInit() {
    this.inputNumber = 1;
    this.fibonacciResult ="1";
    this.itemCount = this.history.length;
    this.result = undefined;
    this.showData();
  }

  fibonacciCompute(numf: number){
    var f  = new Array(numf+1);
    if(numf==0){
      return 0;
    }
    if(numf ==1 || numf ==2){
      f[numf] = 1
      return f[numf]
    }
    if(f[numf]){
      return f[numf];
    }
    var k;
    if(numf & 1){
      k = Math.floor((numf+1)/2); 
    } else{
      k = numf/2;
    }
    if((numf & 1) ){
      f[numf] = (this.fibonacciCompute(k) * this.fibonacciCompute(k) + this.fibonacciCompute(k-1) * this.fibonacciCompute(k-1));
    } else{
      f[numf] = (2*this.fibonacciCompute(k-1) + this.fibonacciCompute(k))*this.fibonacciCompute(k);
    }
    return f[numf];
  }

  
  GetFibonacciNumber(input_number: number, fibonacci_result: string): void{
    if(input_number>0 && input_number<1000){
      var t0: any = performance.now();
      var t1: any = undefined;
      this.fibonacciResult = this.fibonacciCompute(input_number).toString();
      this.flag = false;
      t1 = performance.now();
      this.timeTaken = (t1-t0)/1000;
      const num1: InputNumber = {input_number, fibonacci_result} as InputNumber;
      this._data.getFibonacciNum(num1).subscribe(
        res=>{
          this.showData();
        }
      );
      
    } else{
      this.flag = true;
    }
  }

  showData(){
    this._data.getData().subscribe(data=>{
      this.result = data;
      this.itemCount = this.result.length;
    });
    
  }

}

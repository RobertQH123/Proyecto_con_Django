import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Post } from './Post'

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private HttpClient: HttpClient) { 
    console.log("servicio Working");
  }

  getData(){
    return this.HttpClient.get<Post[]>('http://127.0.0.1:8000/profesionales/query/');
  }
}

import { Component } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'serviciosYa-app';
  posts : any = []; //Se establece el tipo de dato como any para no causar error al ejecutar el servidor
  constructor(private DataService: DataService){
    this.DataService.getData().subscribe(data =>{
      //console.log(data);
      this.posts = data;
    })
  }
}

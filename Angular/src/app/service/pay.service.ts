import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Producto } from '../models/product.model';


@Injectable({
  providedIn: 'root'
})
export class PayService {
  apiUrl = 'http://localhost:8000/api'
  constructor(
    private http: HttpClient
  ) { }

  preference(items: Producto[]){
    console.log(items,"service")
    return this.http.post<{init_point: string}>(`${this.apiUrl}/venta/preference`, {
      items: items})
  }
}

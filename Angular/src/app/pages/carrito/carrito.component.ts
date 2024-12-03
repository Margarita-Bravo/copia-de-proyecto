import { Component, OnInit } from '@angular/core';
import { Producto } from 'src/app/models/product.model';
import { RequestStatus } from 'src/app/models/statusrequest';
import { PayService } from 'src/app/service/pay.service';
import { StoreCartService } from 'src/app/service/store-cart.service';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent implements OnInit {

  products: Producto[] = []
  status: RequestStatus = 'init'
  total_precio = 0
  constructor(
    private serviceStore: StoreCartService,
    private payService: PayService
  ){

  }

  ngOnInit(): void {
      this.serviceStore.myCart$.subscribe(products => {
        this.products = products
        const precio =  products.map(p => p.precio * (p.cantidad ?? 1)).reduce((a, b) => a + b, 0)
        this.total_precio = Number(Number.parseFloat(precio.toString()).toFixed(2))
      })
  }

  preferenceMP(){
    this.status = 'loading'
    this.payService.preference(this.products)
    .subscribe({
      next: (resp) => {
        console.log(resp)
        window.location.replace(resp.init_point)
      },
      error: (error) => {
        this.status = 'failed'
        console.log(error)
      }
    })
  }

}

import { Component, OnInit } from '@angular/core';
import { ProductoService } from 'src/app/service/producto.service'
import { ActivatedRoute, Router } from '@angular/router';
@Component({
  selector: 'app-lista-productos',
  templateUrl: './lista-productos.component.html',
  styleUrls: ['./lista-productos.component.css']
})
export class ListaProductosComponent implements OnInit{

  miProd:any;

  constructor(private prod: ProductoService, private activatedRoute: ActivatedRoute, private router: Router) {
    
  }

  ngOnInit(): void {
    this.prod.traerProductos().subscribe({
      next:(productosTodos)=>{
        this.miProd=productosTodos;
        console.log(" Exito se cargaron los productos");
      },
      error:(errorData)=> {
        console.log("error del componenete producto ");
        console.error(errorData);
        this.router.navigate(['']);
      }
    })

    
  }
  eliminar(produc:any){
    this.miProd.forEach((producto:any)=>{
      if(producto.id== produc.id){
        this.prod.delete(produc.id).subscribe(
          res=>this.prod.traerProductos().subscribe(
            Response=>this.miProd=Response
          )
        );
        console.log('elimino el producto: '+this.miProd.id);
      }
    })

  }

  


}

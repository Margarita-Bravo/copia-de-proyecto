import { Component } from '@angular/core';
import { Servicio } from 'src/app/models/servicio';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ServicioService } from 'src/app/service/servicio.service';


@Component({
  selector: 'app-editar-servicios',
  templateUrl: './editar-servicios.component.html',
  styleUrls: ['./editar-servicios.component.css']
})
export class EditarServiciosComponent {
  servicio: Servicio = Object();

  constructor(private servicioService: ServicioService, private activatedRouter: ActivatedRoute, private router: Router) { }

  ngOnInit(): void {
    const id = this.activatedRouter.snapshot.params['id'];
    this.servicioService.detail(id).subscribe(
      data => {
        this.servicio = data;


      }, err => {
        alert("Error al traer la categoria");
        this.router.navigate(['']);
      }
    )
  }

  guardarNombre(event: any) {
    console.log(this.servicio.nombre = event.target.value)
  }

  guardarDescripcion(event: any) {
    console.log(this.servicio.descripcion = event.target.value)
  }

  guardarPrecio(event: any) {
    console.log(this.servicio.precio = event.target.value)
  }

  guardarFecha(event: any) {
    console.log(this.servicio.fecha_creacion = event.target.value)
  }

  enviarFoto(event: any) {
    console.log(this.servicio.imagen = event.target.files[0])
  }


  onUpdate(): void {

    console.log("se guardo la modificacion del servicio " + this.servicio.nombre);
    console.log("se guardo la modificacion del servicio " + this.servicio.descripcion);
    console.log("se guardo la modificacion del servicio " + this.servicio.precio);
    console.log("se guardo la modificacion del servicio " + this.servicio.fecha_creacion);

    this.servicioService.update(this.servicio.id, this.servicio).subscribe(
      data => {

        console.log("se guardo la modificacion del servicio " + this.servicio.imagen?.name);
        console.log("se al modificar la servicio ", this.servicio);

      }, err => {
        console.log(err)
       
        console.log("Error al modificar la servicio ", this.servicio);
      }
    )
  }






  // submit() {
  // // form = new FormGroup({
  // //   nombre: new FormGroup('', Validators.required),
  // //   imagen: new FormGroup('', Validators.required),
  // //   descripcion: new FormGroup('', Validators.required),
  // //   precio: new FormGroup('', Validators.required),
  // // })
  //   this.servicioService.update(this.servicio.id, this.servicio).subscribe(
  //     data => {
  //       this.servicio.nombre = this.nombre;
  //       this.servicio.descripcion = this.descripcion;
  //       this.servicio.precio = this.precio;
  //       this.servicio.imagen = this.imagen;

  //       console.log(data)
  //       console.log(this.servicio)
  //     }),
  //     (err:any) =>{
  //       console.log(err)
  //       console.log(this.servicio)
  //     }

  //   this.router.navigate(['/lista-servicios'])
  // }
}

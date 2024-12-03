import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ServicioService } from 'src/app/service/servicio.service';
import { Servicio } from 'src/app/models/servicio';


@Component({
  selector: 'app-agregar-servicios',
  templateUrl: './agregar-servicios.component.html',
  styleUrls: ['./agregar-servicios.component.css']
})
export class AgregarServiciosComponent {

  // nuevoServicio: Servicio = new Servicio();
  //servicio :any =[];

  nombre: string = "";
  imagen!: File;
  descripcion: string = "";
  precio: string = "";
  fecha_creacion: string = "";

  constructor(private servicioServicio: ServicioService, private router: Router) {

  }

  ngOnInit(): void { }


  guardarNombre(event: any) {
   console.log( this.nombre = event.target.value)
  }

  guardarDescripcion(event: any) {
    console.log(this.descripcion = event.target.value)
  }

  guardarPrecio(event: any) {
    console.log( this.precio = event.target.value)
  }

  guardarFecha(event: any) {
    console.log(this.fecha_creacion = event.target.value)
  }

  enviarFoto(event: any) {
    console.log(this.imagen = event.target.files[0])
  }


  create() {
    const servicio = new FormData();
    servicio.append('nombre', this.nombre);
    servicio.append('descripcion', this.descripcion);
    servicio.append('precio', this.precio);
    servicio.append('fecha_creacion', this.fecha_creacion);
    servicio.append('imagen', this.imagen,this.imagen!.name);      
    this.servicioServicio.create(servicio).subscribe(()=>
    {
      // Mensaje de exito
      alert('Servicio creado con éxito.');
      this.router.navigate(['/lista-servicios']);
    },
    error => {
      // Mensaje de error
      console.error(error);
      alert('Ocurrió un error al crear el servicio. Por favor, intenta de nuevo.');
      }
  );
      

  }



}


import { FormBuilder,FormControl, Validators, FormGroup } from '@angular/forms';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-contacto',
  templateUrl: './contacto.component.html',
  styleUrls: ['./contacto.component.css'],
})
export class ContactoComponent  implements OnInit {
form: FormGroup;
  constructor(private formBuilder: FormBuilder) {
    this.form = this.formBuilder.group(
      {
        'nombre':['',[Validators.required, Validators.maxLength(20)]],
        'email':['',[Validators.required, Validators.email]],
        'mensaje':['',[Validators.required, Validators.maxLength(150)]]
      }
    )
   }

   get Nombre(){
    return this.form.get("nombre");
   }

   get Email(){
    return this.form.get("email");
   }

   get Mensaje(){
    return this.form.get("mensaje");
   }

   onEnviar(event: Event){
    event.preventDefault;
    if(this.form.valid){
      alert("Enviar al servidor");
    }
    else{
      this.form.markAllAsTouched();
    }
   }

  ngOnInit(): void {
  }

}

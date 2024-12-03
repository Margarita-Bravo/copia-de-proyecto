
const handleMenu = () => {
    const $btnToggle = document.getElementsByClassName('navbar-toggler')
    const $navBar = document.getElementById("navbarNav")
    console.log("js")
    $btnToggle[0]?.addEventListener('click', () => {
        $navBar.style.display === 'block'
            ? $navBar.style.display = 'none' 
            : $navBar.style.display = 'block' 
    })
}

handleMenu();

const validateFormulario = () => {
    const $form = document.querySelector(".needs-validation");
    const $input = document.getElementsByClassName("form-control");
    const $messageInvalid = document.getElementsByClassName("invalid-feedback")
    const $messageValid = document.getElementsByClassName("valid-feedback")

    $form.addEventListener('submit', (e) => {
        e.preventDefault()
        const textregExpr = new RegExp("^[A-z]+$");
        const passwordregExpr = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$/;
        const mailregExpr = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
        let datosValidados = 0;
        let datosAValidar = 0;
        console.log($input[1].required)

        for(let i = 0; i < $input.length; i++){
            if($input[i].required === true && $input[i].value.length === 0 ){
                datosAValidar += 1
                    $messageInvalid[i].style.display = 'block'
                    $messageInvalid[i].textContent = `Este campo no debe estar vacio`
            }else {
                
                let reg = $input[i].type === "text" 
                            ? !textregExpr.test($input[i].value) 
                                : $input[i].type === "email" 
                                    ?  !mailregExpr.test($input[i].value)
                                        : $input[i].type === "password"
                                            ? !passwordregExpr.test($input[i].value)
                                                : none;
                                                
                if(reg){
                    datosAValidar += 1
                        $messageInvalid[i].style.display = 'block'
                        $messageInvalid[i].textContent = $input[i].type === 'password' 
                                                            ? `La contraseña debe tener al menos 1 letra minuscula,  1 letra mayuscula , 1 caracter especial`
                                                            :`Formato de ${$input[i].name} incorrecto`
                }else {
                    $messageInvalid[i].style.display = 'none'
                    $messageValid[i].style.display = 'block'
                    $messageValid[i].textContent =  `Formato de ${$input[i].name} correcto`;
                    datosValidados += 1;
                    if($input[i].type === "password"){
                        if($input[i].value.length < 8 || $input[i].value.length > 15){
                            
                            $messageValid[i].style.display = 'none'
                            $messageInvalid[i].style.display = 'block'
                            $messageInvalid[i].textContent = `La contraseña no debe ser menor que 8 ni mayor que 15 caracteres`
                            datosAValidar += 1
                        }
                    }
                }
            }
        }

        if(datosAValidar === 0){
            alert("El proceso fue realizado con exito")
        }
    }) 
}

validateFormulario()

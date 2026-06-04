/* =========================
   FORM ELEMENTS
========================= */

const loginForm =
document.querySelector(".login-form");

const registerForm =
document.querySelector(".register-form");

const showRegister =
document.getElementById("showRegister");

const showLogin =
document.getElementById("showLogin");


/* =========================
   SHOW REGISTER
========================= */

if(showRegister){

    showRegister.addEventListener("click",()=>{

        loginForm.style.display = "none";

        registerForm.style.display = "block";

        registerForm.classList.add(
            "slide-left"
        );

    });

}


/* =========================
   SHOW LOGIN
========================= */

if(showLogin){

    showLogin.addEventListener("click",()=>{

        registerForm.style.display = "none";

        loginForm.style.display = "block";

        loginForm.classList.add(
            "slide-right"
        );

    });

}


/* =========================
   LOGIN VALIDATION
========================= */

const loginBtn =
document.querySelector(
".login-form button"
);

if(loginBtn){

loginBtn.addEventListener(
"click",
function(e){

e.preventDefault();

const email =
document.querySelector(
".login-form input[type='email']"
);

const password =
document.querySelector(
".login-form input[type='password']"
);

if(
email.value.trim() === "" ||
password.value.trim() === ""
){

alert(
"Please fill all login fields."
);

return;

}

alert(
"Login Successfully!"
);

}
);

}


/* =========================
   REGISTER VALIDATION
========================= */

const registerBtn =
document.querySelector(
".register-form button"
);

if(registerBtn){

registerBtn.addEventListener(
"click",
function(e){

e.preventDefault();

const inputs =
document.querySelectorAll(
".register-form input"
);

let valid = true;

inputs.forEach(input=>{

if(
input.value.trim() === ""
){

valid = false;

}

});

if(!valid){

alert(
"Please fill all fields."
);

return;

}

const password =
inputs[5];

const confirmPassword =
inputs[6];

if(
password.value !==
confirmPassword.value
){

alert(
"Passwords do not match."
);

return;

}

alert(
"Registration Successful!"
);

}
);

}


/* =========================
   PASSWORD SHOW HIDE
========================= */

const passwordInputs =
document.querySelectorAll(
"input[type='password']"
);

passwordInputs.forEach(input=>{

input.addEventListener(
"dblclick",
()=>{

if(
input.type === "password"
){

input.type = "text";

}else{

input.type = "password";

}

}
);

});


/* =========================
   INPUT ANIMATION
========================= */

const allInputs =
document.querySelectorAll(
".input-box input, .input-box select"
);

allInputs.forEach(input=>{

input.addEventListener(
"focus",
()=>{

input.parentElement.style.transform =
"translateY(-3px)";

});

input.addEventListener(
"blur",
()=>{

input.parentElement.style.transform =
"translateY(0)";

});

});
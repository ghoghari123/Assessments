/* =========================
   STICKY HEADER
========================= */

const header = document.querySelector(".header");

window.addEventListener("scroll", () => {

    if(window.scrollY > 80){

        header.classList.add("active");

    }else{

        header.classList.remove("active");

    }

});


/* =========================
   SCROLL TO TOP BUTTON
========================= */

const scrollBtn = document.createElement("div");

scrollBtn.classList.add("scroll-top");

scrollBtn.innerHTML =
'<i class="fa-solid fa-arrow-up"></i>';

document.body.appendChild(scrollBtn);

window.addEventListener("scroll", () => {

    if(window.scrollY > 400){

        scrollBtn.classList.add("show");

    }else{

        scrollBtn.classList.remove("show");

    }

});

scrollBtn.addEventListener("click", () => {

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

});


/* =========================
   ACTIVE NAV LINK
========================= */

const currentPage =
window.location.pathname.split("/").pop();

const navLinks =
document.querySelectorAll(".nav-links a");

navLinks.forEach(link => {

    const href =
    link.getAttribute("href");

    if(href === currentPage){

        link.classList.add("active");

    }

});


/* =========================
   BUTTON RIPPLE EFFECT
========================= */

const buttons =
document.querySelectorAll(
".primary-btn,.register-btn"
);

buttons.forEach(btn => {

    btn.addEventListener("click", function(e){

        const ripple =
        document.createElement("span");

        const rect =
        this.getBoundingClientRect();

        ripple.style.left =
        e.clientX - rect.left + "px";

        ripple.style.top =
        e.clientY - rect.top + "px";

        ripple.classList.add("ripple");

        this.appendChild(ripple);

        setTimeout(() => {

            ripple.remove();

        },600);

    });

});


/* =========================
   PAGE LOADER EFFECT
========================= */

window.addEventListener("load", () => {

    document.body.classList.add("loaded");

});


/* =========================
   SMOOTH SECTION REVEAL
========================= */

const revealElements =
document.querySelectorAll(
"section"
);

const revealObserver =
new IntersectionObserver(

(entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.classList.add(
"show-section"
);

}

});

},

{
threshold:0.15
}

);

revealElements.forEach(section=>{

section.classList.add(
"hidden-section"
);

revealObserver.observe(section);

});
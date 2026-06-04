/* =========================
   SCROLL REVEAL ANIMATION
========================= */

const animatedElements =
document.querySelectorAll(

".destination-card,\
.package-card,\
.feature-card,\
.team-card,\
.value-card,\
.facility-card,\
.contact-card,\
.testimonial-card,\
.award-card,\
.office-card"

);

const animationObserver =
new IntersectionObserver(

(entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.classList.add(
"animate-show"
);

}

});

},

{
threshold:0.2
}

);

animatedElements.forEach(item=>{

item.classList.add(
"animate-hidden"
);

animationObserver.observe(item);

});


/* =========================
   COUNTER ANIMATION
========================= */

const counters =
document.querySelectorAll(
".stat-box h2"
);

const counterObserver =
new IntersectionObserver(

(entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

const counter =
entry.target;

const target =
parseInt(
counter.innerText.replace(/\D/g,"")
);

let count = 0;

const updateCounter = ()=>{

const increment =
target / 80;

if(count < target){

count += increment;

counter.innerText =
Math.ceil(count) + "+";

requestAnimationFrame(
updateCounter
);

}else{

counter.innerText =
target + "+";

}

};

updateCounter();

counterObserver.unobserve(
counter
);

}

});

}

);

counters.forEach(counter=>{

counterObserver.observe(counter);

});


/* =========================
   IMAGE PARALLAX EFFECT
========================= */

window.addEventListener(
"scroll",
()=>{

const images =
document.querySelectorAll(
".hero,.about-hero,.destination-hero,.package-hero,.contact-hero"
);

let scroll =
window.pageYOffset;

images.forEach(image=>{

image.style.backgroundPositionY =
scroll * 0.4 + "px";

});

});


/* =========================
   FLOATING ANIMATION
========================= */

const floatingCards =
document.querySelectorAll(

".destination-card,\
.package-card,\
.feature-card"

);

floatingCards.forEach(card=>{

card.addEventListener(
"mouseenter",
()=>{

card.style.transform =
"translateY(-15px)";

});

card.addEventListener(
"mouseleave",
()=>{

card.style.transform =
"translateY(0px)";

});

});


/* =========================
   GALLERY ZOOM EFFECT
========================= */

const galleryImages =
document.querySelectorAll(
".gallery-item img"
);

galleryImages.forEach(img=>{

img.addEventListener(
"mouseenter",
()=>{

img.style.transform =
"scale(1.12)";

});

img.addEventListener(
"mouseleave",
()=>{

img.style.transform =
"scale(1)";

});

});


/* =========================
   CTA PULSE EFFECT
========================= */

const ctaButtons =
document.querySelectorAll(
".primary-btn"
);

ctaButtons.forEach(btn=>{

setInterval(()=>{

btn.classList.add(
"pulse"
);

setTimeout(()=>{

btn.classList.remove(
"pulse"
);

},1000);

},5000);

});


/* =========================
   PAGE FADE-IN
========================= */

window.addEventListener(
"load",
()=>{

document.body.classList.add(
"page-loaded"
);

});
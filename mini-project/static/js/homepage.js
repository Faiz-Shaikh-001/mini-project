gsap.registerPlugin(ScrollTrigger);

var tl = gsap.timeline();

tl.from("#logo svg, #logo h1, #nav-items h3, #nav-items .btn-hover", {
  y: -100,
  duration: .5,
  opacity: 0,
  stagger: 0.2
})

tl.from("#Hero-text, #Hero-text h1", {
  y: 100,
  stagger: .3,
  opacity: 0,
  duration: 1,
})

gsap.from("#page2 .container1, #page2 .container2", {
  y: 50,
  opacity: 0,
  stagger: .5,
  duration: 3,
  scrollTrigger: {
    trigger: "#page2 .container1, #page2 .container2",
    start: "top 99%",
    toggleActions: "restart none none none"
  },
})

gsap.from("#page3 .footer-container-1, #page3 .footer-container-2", {
  scrollTrigger: {
    trigger: "#page3 .footer-container-1, #page3 .footer-container-2",
    start: "top 99%",
    toggleActions: "restart none none none"
  },
  y: 50,
  opacity: 0,
  stagger: .5,
  duration: 1,
})

function openNav() {
  document.getElementById("mobile-menu").style.height = "100%";
}

function closeNav() {
  document.getElementById("mobile-menu").style.height = "0";
}

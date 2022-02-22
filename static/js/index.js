const header = document.querySelector(".site-header");
const navLink = document.querySelectorAll("header nav li a");
const siteLogo = document.querySelector("header em")

console.log(navLink.length)

window.onscroll = function() {
    if (window.scrollY >= 100) {
        header.classList.add("active");
        for (i = 0; i < navLink.length; i++) {
            navLink[i].classList.add("active");
        }
        siteLogo.classList.add("active");
        
    } else {
        header.classList.remove("active");
        for (i = 0; i < navLink.length; i++) {
            navLink[i].classList.remove("active");
        }
        siteLogo.classList.remove("active");

        
    }
}

// (function () {
//     document.scroll(function () {
//       var nav = $(".navbar-fixed-top");
//       nav.toggleClass('scrolled', this.scrollTop() > nav.height());
//     });
//   });
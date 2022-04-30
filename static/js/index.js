

try {
    const header = document.querySelector(".site-header");
    const navLink = document.querySelectorAll("header nav li a");
    const siteLogo = document.querySelector("header em")
    const siteMenuToggle = document.querySelectorAll(".site-menu-toggle span")

    console.log(navLink.length)

    function iterAdd(arr) {
        for (i=0; i < arr.length; i++) {
            arr[i].classList.add("active")
        }
    }

    function iterRemove(arr) {
        for (i=0; i < arr.length; i++) {
            arr[i].classList.remove("active")
        }
    }

    window.onscroll = function() {
        if (window.scrollY >= 100) {
            header.classList.add("active");
            iterAdd(navLink);
            iterAdd(siteMenuToggle);
            siteLogo.classList.add("active");
            
        } else {
            header.classList.remove("active");
            iterRemove(navLink);
            iterRemove(siteMenuToggle);
            siteLogo.classList.remove("active");            
        }
    }
} catch (err) {
    console.log(err);
}


// //on change hide all divs linked to select and show only linked to selected option
// function getRoom(){
//     //Saves in a variable the wanted div
//     var selector = '.room_' + document.getElementById("room_selector").value;
//     console.log(selector)

//     //hide all elements

//     var collapsibles = document.querySelectorAll('.collapse');

//     for (collapser in collapsibles) {
//         var bsCollapse = new bootstrap
//         collapser.collapse("hide");
//     }

//     //show only element connected to selected option
//     $(selector).collapse('show');
// };
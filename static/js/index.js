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



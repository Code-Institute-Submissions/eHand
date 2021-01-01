document.addEventListener("DOMContentLoaded", function() { 
    let lastScrollTop = 20;
    let nextScrollTop = 150;
    let navbar = document.querySelector(".navbar")

    window.addEventListener("scroll", function () {
        let scrollTop = window.pageYoffset || document.documentElement.scrollTop;
        pageLogo = document.querySelector('#page-logo');
        navLogo = document.querySelector('.navLogo img ');
        background = document.querySelector('nav div .collapse')
        if (scrollTop > lastScrollTop) {
            navbar.style.top ='10px';
            if (scrollTop > nextScrollTop) {
                pageLogo.style.display = 'none';
                navLogo.style.display = 'block';
                background.apply
            }
        } else {
            navbar.style.top ='150px';
            pageLogo.style.display = 'block';
            navLogo.style.display = 'none';
        }
    });
});

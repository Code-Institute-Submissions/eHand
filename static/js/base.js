/*jshint esversion: 6 */ 
document.addEventListener("DOMContentLoaded", function() { 
    let firstScrollTop = 20;
    let nextScrollTop = 150;
    let navbar = document.querySelector(".navbar");
    let pageLogo = document.querySelector('#page-logo img');
    let navLogo = document.querySelector('.navLogo img ');

    /* Handle screen width changes */
    window.addEventListener("resize", function (){
        let scrollTop = window.pageYoffset || document.documentElement.scrollTop;
        let width = window.innerWidth;
        /* if the screen width moves below 768 */
        if (width < 768){
            /* first check if screen is at the top */
            if (scrollTop < firstScrollTop){
                navbar.style.top = '0px';
                pageLogo.style.display = 'block';
                navLogo.style.display = 'none';
                navbar.classList.remove('fixed-navbar');
            }
            /* else its scrolled down */
            else {
                navbar.style.top = '0px';
                pageLogo.style.display = 'none';
                navLogo.style.display = 'block';
                navbar.classList.add('fixed-navbar');
            }
        }
        /* if the screen width moves above 768 */
        else {
            /* first check is screen at the top */
            if (scrollTop < firstScrollTop){
                navbar.style.top ='150px';
                pageLogo.style.display = 'block';
                navLogo.style.display = 'none';
                navbar.classList.remove('fixed-navbar');
            }
            /* else the screen is scrolled down */
            else {
                navbar.style.top = '0px';
                pageLogo.style.display = 'none';
                navLogo.style.display = 'block';
                navbar.classList.add('fixed-navbar');
            }
        }
    });

    /* handle change in scroll */
    window.addEventListener("scroll", function () {
        let scrollTop = window.pageYoffset || document.documentElement.scrollTop;
        let width = window.innerWidth;
        /* if page has been scrolled down past firstScrollTop */
        /* same action for wide or narrow screens */
        if (scrollTop >= firstScrollTop) {
            navbar.style.top = '0px';
            /* check for nextScrollTop */
            if (scrollTop > nextScrollTop) {
                pageLogo.style.display = 'none';
                navLogo.style.display = 'block';
                navbar.classList.add('fixed-navbar');
            }
        /* else - page has not been scrolled and is at the top */
        } else {
            /* first check if we are on large screen size - we should have natural navbar*/
            if (width >= 768) {
                navbar.style.top ='150px';
                pageLogo.style.display = 'block';
                navLogo.style.display = 'none';
                navbar.classList.remove('fixed-navbar');
            }
            /* else we are on small screen size - not scrolled */
            else {
                navbar.style.top ='0px';
                pageLogo.style.display = 'block';
                navLogo.style.display = 'none';
                navbar.classList.remove('fixed-navbar');
            }
        }
    });
});

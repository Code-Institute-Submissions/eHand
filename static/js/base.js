/*jshint esversion: 6 */ 
document.addEventListener("DOMContentLoaded", function() { 
    /** First Handle the navbar - scroll it out of the way on scroll or page resize */
    let firstScrollTop = 20;
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
            pageLogo.style.display = 'none';
            navLogo.style.display = 'block';
            navbar.classList.add('fixed-navbar');
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

    /* fade in out effects for elements */
    const showOptions = {
    threshold: 0.65,
    rootMargin: "0px 0px -30px 0px"
    };

    /** Handle fadin in elements */
    const fadeElements = document.querySelectorAll('.fade-in');
    showWhenScroll = new IntersectionObserver(function (entries, showWhenScroll){
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('show');
                showWhenScroll.unobserve(entry.target);
            }
        });
    }, showOptions);

    fadeElements.forEach(fader => {
        showWhenScroll.observe(fader);

    });

    /** Handle automatic message modal after small delay*/
    setTimeout(function() {
        $("#messageModal").modal('show');
    }, 2000);
});


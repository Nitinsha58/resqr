function toggle(){
    let btn_list = document.getElementsByClassName('alert')

    for (var i=0; i < btn_list.length; i++){
        btn_list[i].style.display = 'none';
    }
}

setTimeout(function (){
    let btn_list = document.getElementsByClassName('alert')

    for (var i=0; i < btn_list.length; i++){
        btn_list[i].style.display = 'none';
    }
}, 7000)


window.onload = function () {
    let menu_btn = document.querySelector(".hamburger");
    let mobile_menu = document.querySelector('#mobile-menu');
    
    menu_btn.addEventListener("click", function () {
        menu_btn.classList.toggle('is-active');
        mobile_menu.classList.toggle('active-menu');
        
        if (document.body.style.overflow === '' ){
            document.body.style.overflow = 'hidden'
        }else {
            document.body.style.overflow = ''
        }
        
    });
}
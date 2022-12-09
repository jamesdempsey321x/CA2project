window.onload = function yoastbreadcrumb() {

    document.getElementById("textyoastadd").innerHTML += "<a id='simpletext'>>></a><a class='responsive-font1' id='textyoastsecond'>Shop</a>"
    document.querySelectorAll('.active').forEach(active => { active.classList.remove('active'); })
    document.getElementById("shopBTN").className = "nav-item active";
}
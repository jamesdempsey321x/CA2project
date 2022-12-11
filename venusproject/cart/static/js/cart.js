window.onload = function yoastbreadcrumb() {

    document.getElementById("textyoastadd").innerHTML += "<a id=" + "simpletext" + ">>></a> <a id=" + "textyoastsecond" + ">Shop</a>"+">>></a> <a id=" + "textyoastsecond" + ">Cart</a>";
    document.querySelectorAll('.active').forEach(active => { active.classList.remove('active'); })
    document.getElementById("cartBTN").className = "nav-item active";
    document.getElementsByClassName("stripe-button-el")[0].className = "btn btn-secondary btn-block my_custom_button"
}

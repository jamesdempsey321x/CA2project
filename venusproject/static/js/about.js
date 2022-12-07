window.onload = function yoastbreadcrumb() {

    document.getElementById("textyoastadd").innerHTML += "<a id=" + "simpletext" + ">>></a> <a id=" + "textyoastsecond" + ">About</a>";
    document.querySelectorAll('.active').forEach(active => { active.classList.remove('active'); })
    document.getElementById("aboutBTN").className = "nav-item active";
}
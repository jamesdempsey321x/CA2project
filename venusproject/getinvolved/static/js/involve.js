window.onload = function yoastbreadcrumb() {

    document.getElementById("textyoastadd").innerHTML += "<a id=" + "simpletext" + ">>></a> <a id=" + "textyoastsecond" + ">Get involved</a>";
    document.querySelectorAll('.active').forEach(active => { active.classList.remove('active'); })
    document.getElementById("involveBTN").className = "nav-item active";
}
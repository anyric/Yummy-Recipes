function addCategory() {
    var cat;

    document.getElementById('addbutton').onclick = openaddcatWindow();

    function openaddcatWindow() {
        if (!cat) {
            cat = window.open("/categorylist", "_blank", "toolbar=no,titlebar=yes,scrollbars=no,resizable=no,top=100,left=500,width=400,height=350");
        }
    }
}

function addRecipe() {
    var rec;
    document.getElementById('addbutton').onclick = openaddrecipeWindow();

    function openaddrecipeWindow() {
        if (!rec) {
            rec = window.open("/recipelist", "_blank", "toolbar=no,titlebar=yes,scrollbars=no,resizable=no,top=100,left=500,width=400,height=350");
        }
    }
}

function back() {
    window.open("/category", "_self");

}

function RefreshParent() {

    window.opener.refresh();
    alert("after")
}

function getid() {
    id = document.getElementById("item").text();
    window.open("/recipe/" + id, "_self");
}

$("#item").on("click", function() {
    var a = $(this).text();
    alert(a);
});
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



$(".cancel_edit").click(function() {
    window.open('', '_parent', '');
    window.close();
});


function getlistvalue() {
    var x = document.getElementsByClassName("list-group-item").text();
    for (i = 0; i < x.length; i++) {
        x[i].onclick = function() {
            console.log(this);
            alert(this);
        }
    }
}


function getid() {
    id = document.getElementById("item").text();
    window.open("/recipe/" + id, "_self");
}

$("#item").on("click", function() {
    var a = $(this).text();
    alert(a);
});
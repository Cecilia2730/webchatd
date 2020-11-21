//$(".btn-minimize").click(function(){
   // $(this).toggleClass('btn-plus');
   // $(".chatt").slideToggle();
  //});

function cerrar(){
 $('#ocultar-y-mostrar').modal('hide');
}

function minimizar() {
    var x = document.getElementById("chatear");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function myFunction() {
    var x = document.getElementById("chatear");
    if (x.style.display === "none") {
        x.style.display = "block";
        } 
    else {
        x.style.display = "none";
        }
}

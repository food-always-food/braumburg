

$(document).ready(function () {
    $(".se-pre-con").fadeOut(5000);
    $("button").click(function () {
        $("p").hide();
        
    });
});

/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "300px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }


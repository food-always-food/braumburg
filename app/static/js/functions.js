$(document).ready(function () {
  //   namespace = '/test';
  $(".se-pre-con").fadeOut(1600);
});

/* Set the width of the side navigation to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "300px";
};

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
};

function expandSus(data) {
  $('div.'+data).toggle();
};

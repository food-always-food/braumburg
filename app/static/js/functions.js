var socket = io();
socket.on('connect', function () {
  socket.emit('my event', {
    data: 'I\'m connected!'
  });
});

$(document).ready(function () {
  //   namespace = '/test';
  $(".se-pre-con").fadeOut(1600);
  var socket = io.connect('http://' + document.domain + ':' + location.port);
  socket.on('connect', function () {
    socket.emit('my_event', {
      data: 'I\'m connected!'
    });
  });
  //   console.log("emitted")
  //   socket.on('refresh feed', function (msg) {
  //     $("#show_comments").append(`<div class="row">
  //     <div class="col">
  //         <h2 class="name">` + msg.title + `</h2>
  //         <h1 class="name">` + msg.first_name + ' ' + msg.last_name + `</h1>
  //     </div>
  // </div>`);
  //   });
});

/* Set the width of the side navigation to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "300px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

// function myFunction(x) {
//   x.classList.toggle("change");
// }
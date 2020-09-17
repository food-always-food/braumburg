var socket = io.connect();
$(document).ready(function () {
    socket.on('connect', function () {
        socket.emit('joined', {
            data: window.location.pathname
        });
    });
    console.log("emitted");
});

socket.on('new-player', function (data) {
    console.log(data);
    className = "." + (data[0].id).toString()
    if ($(className)[0]) {
        $(".col " + data[0].id).html(`
        <h2 class="name">` + data[0].title + `</h2>
        <h1 class="name">` + data[0].first_name + ' ' + data[0].last_name + `</h1>
`)
    } else {
        $(".add-player").append(`<div class="row">
        <div class="col ` + data[0].id + `">
            <h2 class="name">` + data[0].title + `</h2>
            <h1 class="name">` + data[0].first_name + ' ' + data[0].last_name + `</h1>
        </div>
    </div>`)
    }
});
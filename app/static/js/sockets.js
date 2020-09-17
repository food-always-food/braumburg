var socket = io.connect();
socket.close();
socket.open();
var player = 0;
$(document).ready(function () {
    socket.on('connect', function () {
        socket.emit('joined', {
            data: window.location.pathname
        });
    });
});

// socket.on('chatReceived',function (data));

socket.on('chatJoin'),
    function (data) {
        var roomName = data;
    };

socket.on('new-player', function (data) {
    console.log(data)
    player = data[0].id;
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

$('#text').keypress(function (e) {
    var code = e.keyCode || e.which;
    if (code == 13) {
        text = $('#text').val();
        socket.emit('chatSent', {
            data: text,
            "player": player
        });
        $('#text').val('');
    }
});

socket.on('chat', function (data) {
    console.log(data)
    if (data.player === player) {
        $(".chats").append(
            `<div class="row">
            <div class="col">
            <p class="local">` + data.data + `</p>
            </div>
        </div>`
        )
    } else {
        $(".chats").append(
            `<div class="row">
                <div class="col">
                <p class="nonLocal">` + data.data + `</p>
                </div>
            </div>`
        )
    }
});
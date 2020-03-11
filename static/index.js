$(document).ready(function() {
    var socket = io.connect("/");
    //conso
    var count;

    socket.on('connect', function(obj) {

        //console.log(clients.toString());
        //console.log(socket.id);
        playerId = socket.id;
        socket.send(0, null, null, null, socket.id, winner);

    });
    socket.on('message', function(obj) {
        var data = JSON.parse(obj);
        //validPlayer = data.socketid;
        console.log(data.playerscount);
        playerscount = data.playerscount;


        if (data.playerscount == 4) {

            document.getElementById('waiting').innerText = "GAME HAS STARTED!!!";
            window.setTimeout(removewait(), 1000);

            if (playerId == data.socketid[0]) {

                document.getElementById('color').style.color = "red";
                document.getElementById('color').innerText = "YOUR COLOR IS RED";

            }
            if (playerId == data.socketid[1]) {
                document.getElementById('color').style.color = "blue";
                document.getElementById('color').innerText = "YOUR COLOR IS BLUE";
            }
            if (playerId == data.socketid[2]) {
                document.getElementById('color').style.color = "yellow";
                document.getElementById('color').innerText = "YOUR COLOR IS YELLOW";
            }
            if (playerId == data.socketid[3]) {
                document.getElementById('color').style.color = "green";
                document.getElementById('color').innerText = "YOUR COLOR IS GREEN";
            }
            var text1 = document.getElementById('player').innerText;
            if (text1 == 'red')
                validPlayer = data.socketid[0];
            if (text1 == 'blue')
                validPlayer = data.socketid[1];
            if (text1 == 'yellow')
                validPlayer = data.socketid[2];
            if (text1 == 'green')
                validPlayer = data.socketid[3];
            //  console.log(text1);
            if (data.dice != 0) {
                num = data.dice;

                //var temp = text;
                // console.log(num);

                diceRol();
                //if (temp != document.getElementById('player').innerText)
                randomMove(data.color, data.pawnno);

                //console.log(playerId);
            }
            var text2 = document.getElementById('player').innerText;
            // console.log(text2);
            if (text2 == 'red')
                validPlayer = data.socketid[0];
            if (text2 == 'blue')
                validPlayer = data.socketid[1];
            if (text2 == 'yellow')
                validPlayer = data.socketid[2];
            if (text2 == 'green')
                validPlayer = data.socketid[3];

            //console.log(text);
        } else
            document.getElementById('waiting').innerText = "WAITING FOR OTHER PLAYERS...";
    });
    $('#dice').on('click', function() {
        if (validPlayer == playerId && playerscount == 4) {

            var text = document.getElementById('player').innerText;
            socket.send(num, null, null, text, null, winner);
        }
    });

    $('#yellowpawn1').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'yellow', 1, text, null, winner)
        }
    });
    $('#yellowpawn2').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'yellow', 2, text, null, winner)
        }
    });
    $('#yellowpawn3').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'yellow', 3, text, null, winner)
        }
    });
    $('#yellowpawn4').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'yellow', 4, text, null, winner)
        }
    });
    $('#redpawn1').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, "red", 1, text, null, winner);
        }
    });
    $('#redpawn2').on('click', function() {

        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'red', 2, text, null, winner)
        }
    });
    $('#redpawn3').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'red', 3, text, null, winner)
        }
    });
    $('#redpawn4').on('click', function() {
        if (validPlayer == playerId) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'red', 4, text, null, winner)
        }
    });
    $('#bluepawn1').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, "blue", 1, text, null, winner);
        }
    });
    $('#bluepawn2').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'blue', 2, text, null, winner)
        }
    });
    $('#bluepawn3').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'blue', 3, text, null, winner)
        }
    });
    $('#bluepawn4').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'blue', 4, text, null, winner)
        }
    });
    $('#greenpawn1').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, "green", 1, text, null, winner);
        }
    });
    $('#greenpawn2').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'green', 2, text, null, winner)
        }
    });
    $('#greenpawn3').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'green', 3, text, null, winner)
        }
    });
    $('#greenpawn4').on('click', function() {
        if (validPlayer == playerId && clicked == true) {
            var text = document.getElementById('player').innerText;
            socket.send(num, 'green', 4, text, null, winner)
        }
    });



});
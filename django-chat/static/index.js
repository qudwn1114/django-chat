document.querySelector('#room-name-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
    }
};

document.querySelector('#room-name-submit').onclick = function(e) {
    let roomName = document.querySelector('#room-name-input').value;
    window.location.pathname = '/chat/' + roomName + '/';
};
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


window.addEventListener('load', function(){
    //채팅방 메세지 초기화
    document.getElementById('chat-messages').innerHTML = '';
    $.ajax({
        type: "GET",
        url: `/message/${room_id}/`,
        headers: {
            'X-CSRFToken': csrftoken
        },
        datatype: "JSON",
        success: function(data) { 
            for(let i=0; i < data.message_list.length; i++){
                displayMessage(data.message_list[i]);
            }
        },
        error: function(error) {  
            alert(error.status + JSON.stringify(error.responseJSON));
        },
    });
    document.getElementById('chat-message-input').focus();
});

let httpProtocol = 'http://'; 
let wsProtocol = 'ws://';
if (window.location.protocol === 'https:') {
    httpProtocol = 'https://';
    wsProtocol = 'wss://';
}
const chatSocket = new WebSocket(
    `${wsProtocol}${window.location.host}/ws/chat/${room_id}/`
    );  

chatSocket.onmessage = (e) => {
    const data = JSON.parse(e.data);
    displayMessage(data);
};

chatSocket.onclose = (e) => {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').addEventListener("click",(e) => {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    if (message) {
        const messagePayload = {
            'room_id': room_id,
            'user_id': user_id,
            'message': message,
        };

        chatSocket.send(JSON.stringify(messagePayload));
        messageInputDom.value = '';
    }
});


//메세지 디스플레이
function displayMessage(data){
    let today = new Date()
    today = today.toISOString().split('T')[0];
    let div_class = 'chat-message-right';
    let username = 'You'
    if(data.userId != user_id){
        div_class = 'chat-message-left';
        username = data.username;
    }
    let createdAt = data.createdAt;
    if(createdAt.length > 5){
      let s = createdAt.split(" ");
      if (s[0] == today){
        createdAt = s[1].substr(0, 5);
      }
      else{
        createdAt = s[0] + s[1].substr(0, 6);
      }
    }
    let div = `
    <div class="${div_class} pb-4">
        <div>
            <img src="/static/image/person.png" class="rounded-circle mr-1" alt="Chris Wood" width="40" height="40">
            <div class="text-muted small text-nowrap mt-2">${createdAt}</div>
        </div>
        <div class="flex-shrink-1 bg-light rounded py-2 px-3 mr-3">
            <div class="font-weight-bold mb-1">${username}</div>
            ${data.message}
        </div>
    </div>
    `;
    let message_div = document.getElementById('chat-messages')
    message_div.innerHTML += div;
    message_div.scrollTop = message_div.scrollHeight;
}

function leave(){
    if (!confirm("Are you sure you want to leave?")) {
        return;
    }
    $.ajax({
        type: "POST",
        url: `/leave/${room_id}/`,
        headers: {
            'X-CSRFToken': csrftoken
        },
        datatype: "JSON",
        success: function(data) { 
            alert(data.message);
            location.href=data.url;
        },
        error: function(error) {  
            if(error.status == 401){
                alert('Sign in please');
            }
            else{
                alert(error.status + JSON.stringify(error.responseJSON));
            }
        },
    });

}
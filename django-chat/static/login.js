const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const username = document.getElementById("username");
const password = document.getElementById("password");
const btn_submit = document.getElementById("btn-submit");


btn_submit.addEventListener("click", () => {
    const data = new FormData(document.getElementById("login_form"));
    if (validation() == false) {
        return;
    }
    username.disabled = true;
    password.disabled = true;
    btn_submit.disabled = true;

    $.ajax({
        type: "POST",
        headers: {
            'X-CSRFToken': csrftoken
        },
        url: "",
        data: data,
        enctype: "multipart/form-data", //form data 설정
        processData: false, //프로세스 데이터 설정 : false 값을 해야 form data로 인식
        contentType: false, //헤더의 Content-Type을 설정 : false 값을 해야 form data로 인식
        success: function (data) {
            alert(data.message);
            location.href=data.url;
        },
        error: function (error) {
            alert(error.responseJSON.message);
            username.disabled = false;
            password.disabled = false;
            btn_submit.disabled = false;
        },
    });


});


//유효성 체크 함수
function validation() {
    if (username.value == "") {
        alert('Input ID, please.');
        username.focus();
        return false;
    }
    if (password.value == "") {
        alert('Input Password, please.');
        password.focus();
        return false;
    }
    return true;
}

function enterkey(event) {
    if (window.event.keyCode == 13) {
        btn_submit.click()
    }
}
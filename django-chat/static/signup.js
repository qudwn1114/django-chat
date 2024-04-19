const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const username = document.getElementById("username");
const membername = document.getElementById("membername");
const password = document.getElementById("password");
const btn_submit = document.getElementById("btn-submit");



btn_submit.addEventListener("click", () => {
    const data = new FormData(document.getElementById("signup_form"));
    if (validation() == false) {
        return;
    }
    username.disabled = true;
    password.disabled = true;
    membername.disabled = true;
    btn_submit.disabled = true;
    btn_submit.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';

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
            membername.disabled = false;
            btn_submit.disabled = false;
            btn_submit.innerHTML = 'Sign up';
        },
    });


});


//유효성 체크 함수
function validation() {
    if (membername.value == "") {
        alert('Input your Name, please.');
        membername.focus();
        return false;
    }
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
    if (!regPassword(password.value)) {
        password.focus();
        return false;
    }
    return true;
}


//비밀번호 정규식
function regPassword(str) {
    if (!/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$/.test(str)) {
        alert('The password must be 8 to 16 characters long and contain one letter and one number.');
        return false;
    }
    return true;
}
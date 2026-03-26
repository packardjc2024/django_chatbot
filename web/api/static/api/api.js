$(document).ready(()=> {
    $('#password-submit').click((event)=> {
        event.preventDefault();
        createSecret();
    });
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function createSecret(){
    let app = $('#application').val();
    let pw = $('#password').val();
    $('#application').val('');
    $('#password').val('');
    console.log(pw);

    console.log('credentials gathered, sending to backend...')

    $.ajax({
        url: '/api/add_credentials/',
        type: 'POST',
        data: {'application': app, 'password': pw},
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success: (response)=> {
            $('#password-container').toggle();
            $('#results-container').toggle();
            $('#encryption-key').text(response.key)
        },
        error: (xhr, status, error)=> {
            console.log(error);
        }
    });
}
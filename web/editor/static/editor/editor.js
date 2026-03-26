// $(document).ready(()=> {
//     $('.toolbar-p').click(function(event) {
//         event.preventDefault();
//         let selectedOption = $(this).text();
//         getForm(selectedOption);
//     });
// });

// $(document).ready(function() {
//     let height = $('#full-navbar').data('height');
//     $('#full-navbar, #small-navbar').css({'min-height': `${height}px`});
// });


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

// function getForm(sectionName) {
//     $.ajax({
//         url: '/editor/',
//         type: 'POST',
//         data: {'section': sectionName},
//         headers: {'X-CSRFToken': getCookie('csrftoken')},
//         success: (response)=> {
//             $('#form-container').empty();
//             $('#form-container').append(response['html']);
//         },
//         error: (xhr, status, error)=> {
//             console.log(error);
//         }
//     });
// }
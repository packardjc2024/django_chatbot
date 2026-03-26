$(document).ready(function() {
    $('#prompt').focus();
    $('#prompt').on('keydown', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            let userInput = $('#prompt').val()
            $('#chat-history').append(`<div class="user"><p>${userInput}</p></div>`);
            $('#chat-history').append('<div class="model"><p>Thinking...</p></div>');
            $('#chatbot-form').submit(); 
        }
    });
});


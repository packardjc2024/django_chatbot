$(document).ready(() => {
    $('#small-navbar-menu-icon').on('click', dropDownMenu);
});

function dropDownMenu(){
    if ($('#small-navbar-dropdown-container').css('display') === 'none'){
        $('#small-navbar-dropdown-container').css('display', 'flex');
    } else {
        $('#small-navbar-dropdown-container').css('display', 'none')
    }
}
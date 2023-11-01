document.addEventListener('DOMContentLoaded', function () {
    function translateHello() {
        const langCode = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + langCode, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translateHello);

    $('#language_code').keypress(function(e) {
        if (e.which === 13) {
            translateHello();
        }
    });
});

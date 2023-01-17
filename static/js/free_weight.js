
$(init);

var callback_form_html = '<div id="fade_div" style="position: absolute; top: 0; left: 0; height: 100%; width: 100%; background-color: rgba(30, 30, 30, 0.5); z-index: 1000">'

                       + '<form id="callback_form" onSubmit="try_PS">'
                       + '<div class="call_greet">Ваше имя: </div>'
                       +     '<input type="text" name="call_name" id="call_name"><br />'
                       +     '<div class="call_greet">Телефонный номер: </div>'
                       +     '<input type="text" name="phone" id="call_phone"><br />'
                       +     '<div id="call_back_buttons">'
                       +          '<input type="button" class="call_button" name="call_cancel" id="call_cancel" value="Отмена">'
                       +          '<input type="button" class="call_button" name="call_send" id="call_send" value="Отправить">'
                       +     '</div>'
                       + '</form>'

                       + '</div>'

var call_greet_css = {
                         "float": "left",
                         "text-align": "right",
                         "margin-right": "20px",
                         "margin-bottom": "5px",
                         "min-width": "35%",
                         "font-size": "0.9em"
                     };

var call_button_css = {
                         "margin": "30px"
                     };

var callback_buttons_css = {
                         "text-align": "center"
                     };

var call_input_css = {
                         "margin-bottom": "10px"
                     };

var callback_form_css = {
                             "display": "block",
                             "position": "absolute",
                             "top": "50%",
                             "left": "50%",
                             "width": "400px",
                             "margin-left": "-200px",
                             "height": "100px",
                             "margin-top": "-100px",
                             "background-color": "#ffffff",
                             "padding": "20px",
                             "border-radius": "10px",
                             "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                         };

function hide_callback_form(){
    $('#fade_div').hide();
}

function callback_click_handler(){
    alert($('#flag').css("color"));
    alert($('#flag').length);
}

function show_callback_form(){
    tmp1 = $('#fade_div');
    if (tmp1.length) {
        tmp1.show();
    } else {
        $('body').append(callback_form_html);
        call_back_form = $('#callback_form');
        $('#fade_div').click(callback_click_handler);
        $('#callback_form').click(function(){alert('PshPsh');});
        call_back_form.css(callback_form_css);
        $('.call_greet').css(call_greet_css);
        $('.call_button').css(call_button_css);
        $('#call_name').css(call_input_css);
        $('#call_back_buttons').css(callback_buttons_css);
        $('#call_cancel').click(hide_callback_form);
        $('body').append('<div id="flag" style="color: red">LALALALALA</div>');
        alert('Ready');
    };


}

function try_PS(event) {
    event.preventDefault();
    alert('Stop');
}

function init(){
    tmp2 = $('.m-callback');
    tmp2.css('cursor', 'pointer');
    tmp2.click(show_callback_form);
}

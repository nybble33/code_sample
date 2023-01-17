function tinyDjangoBrowser(field_name, url, type, win) {
    var managerURL = window.location.toString()
            + '../../../cms/image/?type=' + type;

    tinyMCE.activeEditor.windowManager.open({
        file: managerURL,
        title: 'Кликните на эскиз нужной картинки',
        width: 800,
        height: 450,
        resizable: 'yes',
        inline: 'yes',
        close_previous: 'no',
        popup_css : false
    }, {
        window: win,
        input: field_name
    });

    return false;
}

$(document).ready(function() {
    $("#id_keywords").css("height", "45px");
    $("#id_description").css("height", "45px");
    $("#id_content").css("height", "600px");
    $("#id_content").css("width", "72em");
    $("#id_title").css("width", "50em");
    $("#id_slug").css("width", "50em");
    $('#id_content_type').bind('change', function() {
        set_tinymce_status();
    });
    //set_tinymce_status();
    tinymce_init();
});

function set_tinymce_status() {
    /*
        if ($('#id_content_type').val() == 1) {
            tinymce_init();
        } else {
            tinyMCE.execCommand('mceFocus', false, 'id_content');
            tinyMCE.execCommand('mceRemoveControl', false, 'id_content');
        }
    */
}

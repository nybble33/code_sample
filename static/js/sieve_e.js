//

var MAX_NUM = 10;

function clear_sieve(){
    $("#sieve").text("");
};

function fill_sieve(_max_num){
    MAX_NUM = parseInt(_max_num);
    clear_sieve();
    el_str = ''
    for (i=1; i<=MAX_NUM; i++){

        el_str += el_prefix(i);
        el_str += "<div class=\'col s1 center"+offset(i)+"\'>"
        el_str +=   "<span id=\'cell_"+i+"\' class=\'card-panel teal lighten-4 red-text\'>";
        el_str +=     (i);
        el_str +=   "</span>";
        el_str += "</div>";
        el_str += el_suffix(i, MAX_NUM);

    };
    $(el_str).appendTo('#sieve');
};

function cell_is_simple(_num){
    //alert(($"#cell_"+_num));
    if ($("#cell_"+_num).hasClass('teal')||
       $("#cell_"+_num).hasClass('blue')){
        return true;
    } else {
        return false;
    };
};

function cell_is_composite(_num){
    if ($("#cell_"+_num).hasClass('grey')){
        return true;
    } else {
        return false;
    };
}

function el_prefix(num){
    if (is_divident(num-1, 10)){
        return "<div class=\'row\'>";
    } else {
        return '';
    };
};

function el_suffix(num, max){
    if (is_divident(num, 10) || (num == max)){
        return '</div><br><br>';
    } else {
        return '';
    }
}

function offset(num){
    if (is_divident(num-1, 10)){
        return(' offset-s1');
    } else {
        return '';
    };
}

function is_divident(number, part){
    return parseInt(number/part)*part == number;
};

function light_up_cell(cell_no){
    cell_id = 'cell_' + cell_no;
    if ($('#'+cell_id).hasClass('teal')){
        $("#"+cell_id).removeClass('teal lighten-4 red-text');
        $("#"+cell_id).addClass('blue darken-4 white-text');
    };
}

function put_out_every(start_cell){
    for (i=start_cell*2; i<=MAX_NUM; i+=start_cell){
        put_out_cell(i);
    }
};

function put_out_cell(cell_no){
    cell_id = 'cell_' + cell_no;
    if ($('#'+cell_id).hasClass('teal')){
        $("#"+cell_id).removeClass('teal red-text');
        $("#"+cell_id).addClass('grey grey-text');
    };
}

function go_sieve(){
    put_out_cell(1);
    light_up_cell(2);
    for (j=2; j<=MAX_NUM; j++){
        if (cell_is_simple(j)){
            light_up_cell(j);
            put_out_every(j);
        };
    };
};

$(document).ready(function(){

    $("#swBtn").on("click", function(){
        foo = parseInt($("#swNum").val());
        go_sieve();
    });

    $("#startBtn").on("click", function(){
        foo = parseInt($("#maxNum").val());
        fill_sieve(foo);
    });

});

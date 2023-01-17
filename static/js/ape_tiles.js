
function not_null(arg, r_arg){
    if (arg) {return arg} else {return r_arg}
}

function show_tiles(tile_props){
    if (!tile_props) {tile_props={}};
    var first_run = true;
    var tiles = $('.'+not_null(tile_props.div_class, 'my_tile'));
    tiles.each(function(i, elem){
        tmp = $(elem).html();
        this_id = 'tile_'+i;
//        alert(this_id);
        tmp = '<div id="'+this_id+'" class="tile_outer">'+tmp+'</div>';
        $(elem).html(tmp);
        if (first_run){
            $('head').append('<style>.my_tile{width: 500px;height: 200px;border: 1px solid #000; overflow: hidden;}.my_tile>div{color: #f00;overflow: hidden;width: 900px;height: 200px; position: relative;left:0px; transition: left 1s ease-out 0.1s;}.my_tile>div:hover{left: -400px;}.my_tile>div>div{color: #00f;float: left;width: 400px;height: 150px;border: 1px solid #00f;</style>');
//            alert('First Run');
            first_run = false;

        };
    });
}

//show_tiles({'div_class':'Ololo'});
//show_tiles();
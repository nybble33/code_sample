// Binary mouse code

//let dose = [];
var dose = [[], [], [], [], [], [], [], [], [], []];
var _poisonedTube = 0;
var deadMouseColor = "grey";
var deadMouseTextColor = "white-text";
var deadMouseText = "R.I.P";

function bin(foo){
  if (foo < 2){
    return foo;
  } else {
    return String(bin(~~(foo/2)))+String(foo%2);
  }
}

function toTenDigits(num){
  return '0000000000'.substr(String(num).length) + String(num)
}

function makeDoses() {
  for (i=1; i<= 1000; i++){
    for (j=0; j<=9; j++){
      _tubeNo = toTenDigits(bin(i));
      if (_tubeNo[j]=='1'){
        //alert('Push - ')
        dose[9-j].push(i);
      }
    }
    //alert('Waiting');
  }
}

function isDead(mouseNo){
  for (i1=0; i1<dose[mouseNo].length;i1++){
    if (dose[mouseNo][i1]==_poisonedTube){
      return true;
    }
  }
  return false;
}

function reviveMouses(){
  for (i2=0; i2<10; i2++){
    $("#mouse_"+i2).removeClass(deadMouseColor+" "+deadMouseTextColor);
    $("#mouse_"+i2+">span").html("");
  }
}

function killMouse(mouseNo){
  if (!$("#mouse_"+mouseNo).hasClass(deadMouseColor)){
    $("#mouse_"+mouseNo).addClass(deadMouseColor+" "+deadMouseTextColor);
    $("#mouse_"+mouseNo+">span").html(deadMouseText);
  }
}

function findPoison(){
  //bar = toTenDigits(bin(parseInt($("#tubeNo").val())));
  //alert(bar+" -- "+bar[6]);
  reviveMouses();
  _poisonedTube = parseInt($("#tubeNo").val());
  makeDoses();
  //dose[0].push(123);
  /*
  alert("Yo ho ho");
  for (i=0; i<10; i++){
    alert(i+" - "+isDead(i));
  }
  */
  for (i=0; i<=9; i++){
    //$('#mouse_house').append("<li> -- "+dose[i]+" -- "+isDead(i)+"</li>");
    if (isDead(i)){
      killMouse(i);
    }
  }
}

$(document).ready(function(){

  $("#poisonTube").on("click", function(){
    findPoison();
  });

  $("#randomPoison").on("click", function(){
    $("#tubeNo").val(parseInt(Math.random()*1000+1));
    findPoison();
  })

})

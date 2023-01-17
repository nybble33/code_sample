
  var EARHT_WIDTH = 200;
  var EARHT_HEIGHT = 200;
  var COLONY_WIDTH = 5;
  var COLONY_HEIGHT = 5;
  var alive_color = "#000";
  var dead_color = "#FFF";

function random_alive(){
  return Math.random()>0.5 ? true: false;
};

class Cell {
  constructor(alive){
    this.alive = typeof alive == 'undefined' ? 
      random_alive(): alive;
    this.width = EARHT_WIDTH/COLONY_WIDTH;
    this.height = EARHT_HEIGHT/COLONY_HEIGHT;
  };
  set_random_status = function(){
    foo = Math.random();
    if (foo>0.75 || foo<0.25){
      this.alive = true;
    }
    else{
      this.alive = false;
    };
  };
  get status(){
    return this.alive ? 'alive': 'dead';
  };
  get html(){
    return `<div class='cell ${this.status}'></div>`
  };
};
/*
class Resident extends Cell{

};
*/
class Earth{
  constructor(cols, rows){
    this.width = cols;
    this.height = rows;
    this.population = [];
    for (var i=0; i<rows; i++){
      this.population[i] = [];
      for (var j=0; j<rows; j++){
        this.population[i][j] = new Cell();
      };
    };
  };
  //population = [];
}

class Resident {
  constructor(name){
    this.name = name;
    this.up_neigbour = '--';
  };
  set up_neigbour(some_resident){
    if (some_resident != '--'){
      this.up_neigbour = some_resident;
    };
  };
  get up_neigbour(){
    return this.up_neigbour;
  }
}

$(document).ready(function(){
  /*
  ROW_NUM = 50;
  cells = [];
  for (i=0; i<ROW_NUM; i++){
    cells[i] = new Cell();
    //cells[i].set_random_status();
  };
  for (i=0; i<ROW_NUM; i++){
    // ~alert(cells[i].get_html());
    $(cells[i].html).appendTo("#earth");
  };
  */
  /*
  var Eee = new Earth(5, 5);
  alert(Eee.population[2][2].status);
  */
  var vasya = new Resident('Vasya');
  var petya = new Resident('Petia');
  vasya.up_neigbour = petya;
  alert(`${vasya.name}'s up neigbour is ${vasya.up_neigbour.name}`);
});

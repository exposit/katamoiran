
var randomElement = function(elem, passed){
  debugger;

  // var base = new Array('ranelem','and','so','if','or','but','then');
  //
  // var first = Array.apply(null, Array(3)).map(String.prototype.valueOf,"hi");
  //
  // var firstbase = base.concat(first)
  //
  // var final = firstbase.concat(passed);

  passed.sample(elem);

};

Array.prototype.sample = function(elem){

    var raw = this[Math.floor(Math.random()*this.length)];
    var split = raw.split('~');
    document.getElementById(elem + '_head').innerText = split[0];
    document.getElementById(elem + '_body').innerText = split[1];
};

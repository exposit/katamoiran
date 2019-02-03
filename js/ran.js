var randomElement = function(elem, passed){
  debugger;
  passed.sample(elem);

};

Array.prototype.sample = function(elem){

    var raw = this[Math.floor(Math.random()*this.length)];
    document.getElementById(elem + '').innerText = raw;
};

var randomTwoPartElement = function(elem, passed){
  debugger;
  passed.samplesplit(elem);

};

Array.prototype.samplesplit = function(elem){

    var raw = this[Math.floor(Math.random()*this.length)];
    var split = raw.split('~');
    document.getElementById(elem + '_head').innerText = split[0];
    document.getElementById(elem + '_body').innerText = split[1];
};

var randomPrefixElement = function(elem, passed){
  debugger;
  passed.sampleprefix(elem);

};

Array.prototype.sampleprefix = function(elem){

    var base = new Array('and','so','if','or','but','then');
    var pref = base[Math.floor(Math.random()*base.length)];
    var raw = this[Math.floor(Math.random()*this.length)];
    var output =`[${pref}] ${raw}`
    document.getElementById(elem + '').innerText = output;
};

var randomMultiElement = function(elem, a, b, c, d){
  debugger;
  var rawa = a[Math.floor(Math.random()*a.length)];
  var rawb = b[Math.floor(Math.random()*b.length)];
  var rawc = c[Math.floor(Math.random()*c.length)];
  var rawd = d[Math.floor(Math.random()*d.length)];
  var output =`${rawa} ${rawb} ${rawc} ${rawd}`
  document.getElementById(elem + '').innerText = output;
};

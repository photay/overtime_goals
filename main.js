
function readData(){
  var file = "World_Cup_Stats_2018.csv";
  d3.csv(file, function(vals)){
    console.log(vals);
  })

}

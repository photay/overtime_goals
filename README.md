# overtime_goals

d3.csv(sim_file).row(function(d){
    return {key: d.key, value: +d.value};
  })

  // data.forEach(function(d){
  //   d.year = new Date(+d.Year, 0, 1);
  //   d.make = d.Make;
  //   d.model = d.Model;
  //   d.length = +d.Length;
  // });

  // return {
  //   year: new Date(+d.Year, 0, 1),
  //   make: d.Make,
  //   model: d.Model,
  //   length: +d.Length
  // };
}, function (dataset) {
  // d3.select("div")
  //   .html("<p>"+data.Make+"</p>")

  d3.select("div")
    .selectAll("p")
    .data(dataset)
    .enter()
    .append("p")
    .text("New Paragraph!");
    // .text(function(d) {
    //     return d.Make;
    // });
  console.log(dataset);
  console.log(1);
});

// function printData(data){
//   d3.select("div")
//     .selectAll("p")
//     .data(data)
//     .enter()
//     .append("p")
//     .text("New Paragraph!");
//     // .text(function(d) {
//     //     return d.Make;
//     // });

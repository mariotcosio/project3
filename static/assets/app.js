    var svgWidth = window.innerWidth;
    var svgHeight = window.innerHeight;

    var margin = {
        top: 20,
        right: 40,
        bottom: 80,
        left: 100
    };

    var width = svgWidth - margin.left - margin.right;
    var height = svgHeight - margin.top - margin.bottom;

    var svg = d3
        .select(".chart")
        .append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight);

    var chartGroup = svg.append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

function makeResponsive() {   

    /*function updateToolTip(data, circlesGroup) {
        var toolTip = d3.tip()
          .attr("class", "tooltip")
          .offset([80, -60])
          .html(function(d) {
            return (`${data.IUCN} TEST `);
          });
      
        circlesGroup.call(toolTip);
      
        circlesGroup.on("mouseover", function(data) {
          toolTip.show(data);
        })
          // onmouseout event
          .on("mouseout", function(data, index) {
            toolTip.hide(data);
          });
      
        return circlesGroup;
      }*/

    // import data
    d3.csv("Resources/WILD_LIFE.csv").then(function(data){

        // Define the div for the tooltip
        var div = d3.select("body").append("div")	
        .attr("class", "tooltip")				
        .style("opacity", 0);
        
        var IUCN=[];
        data.forEach(function(d){
            d.Value= +d.Value;
            IUCN.push(d.IUCN);

        });
        
        var xLinearScale = d3.scaleLinear()
        // .domain([1, d3.max(data, d => d.Value)])
        .domain([1, 400])
        .range([5, width]); 
        

        var yBandScale = d3.scaleBand()
            .domain(IUCN)
            .range([0, height]);

            var xAxis = d3.axisBottom(xLinearScale);
            var yAxis = d3.axisLeft(yBandScale );
            
        chartGroup.append("g")
                .attr("transform", `translate(0, ${height})`)
                .call(xAxis);
                
        chartGroup.append("g")
                .call(yAxis);

        var circlesGroup = chartGroup.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", d => xLinearScale(d.Value))
            .attr("cy", d => yBandScale(d.IUCN))
            .attr("r", d => xLinearScale(d.Value/30))
            .attr("fill", "pink")
            .attr("opacity", ".5");

        circlesGroup.on("mouseover", function(data,i){
            d3.select(this)
            .transition()
            .duration(1000)
            .attr("r",d => xLinearScale(d.Value/20))
            .attr("fill","red");

            div.transition()		
            .duration(200)		
            .style("opacity", .9);		
            div.html(`${data.IUCN}, ${data.Value}, ${data.SPEC}, ${data.alpha3}  `)	
            .style("left", (d3.event.pageX) + "px")		
            .style("top", (d3.event.pageY - 28) + "px");
        })
            .on("mouseout", function(){
                d3.select(this)
                    .transition()
                    .duration(1000)
                    .attr("r", d => xLinearScale(d.Value/30))
                    .attr("fill", "pink");
                div.transition()		
                .duration(500)		
                .style("opacity", 0);	
            });
        
    /*-------------*/
  /*var toolTip = d3.select("body").append("div").attr("class", "tooltip");

  circlesGroup.on("mouseover", function(data, i) {
    toolTip.style("display", "block");
    toolTip.html(`Status: <strong>${data.IUCN}</strong>`)
      .style("left", d3.event.pageX + "px")
      .style("top", d3.event.pageY + "px");
      toolTip.show(data);
  })
    // Step 3: Add an onmouseout event to make the tooltip invisible
    .on("mouseout", function() {
      toolTip.style("display", "none");
    });*/
            
// alert(d3.event.pageX);
console.log(circlesGroup);

// Step 2: Add an onmouseover event to display a tooltip
// ========================================================
//   circlesGroup.on("mouseover", function(data, i) {
//     toolTip.style("display", "block");
//     toolTip.html(`Status: <strong>${data.IUCN}</strong>`)
//       .style("left", d3.event.pageX + "px")
//       .style("top", d3.event.pageY + "px");
//   })
//     // Step 3: Add an onmouseout event to make the tooltip invisible
//     .on("mouseout", function() {
//       toolTip.style("display", "none");
//     });
    /*------------*/
    });
}

// When the browser loads, makeResponsive() is called.
makeResponsive();

// When the browser window is resized, responsify() is called.
d3.select(window).on("resize", makeResponsive);


// // transition on page load
// chartGroup.selectAll("circle")
//   .transition()
//   .duration(1000)
//   .attr("cx", (d, i) => xScale(i))
//   .attr("cy", d => yScale(d));


function openPage(name) {
    alert(name);
}
 


/* ---------------------------- */
var data = [
    {
        place: "USA",
        spieces: "Mamals",
        condition: "Critical",
        number: "20"
    },

    {
        place: "Australia",
        spieces: "Mamals",
        condition: "Endangered",
        number: "200"
    }
];
// send unique values from each data set
// var arr1=[];

// function init(){
//     alert("in");
//     var selector1 = d3.select("#places-menu");
//     var selector2 = d3.select("#spieces-menu");
//     var selector3 = d3.select("#condition-menu");
 
//     data.forEach(row => {
//         selector1
//             .append('a')
//             .attr("class","dropdown-item")
//             .text(row.place);
    
//     selector2
//             .append('a')
//             .attr("class","dropdown-item")
//             .text(row.spieces);
    
//     selector3
//             .append('a')
//             .attr("class","dropdown-item")
//             .text(row.condition)
//             arr1.push(row.place);
//     });
//     // alert(arr1);
// }

// init();

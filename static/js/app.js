var svgWidth = 960;
var svgHeight = 500;

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
  
// import data
d3.csv("Resources/WILD_LIFE.csv").then(function(data){
    var IUCN=[];
    data.forEach(function(d){
        d.Value= +d.Value;
        IUCN.push(d.IUCN);

    });
    
    var xLinearScale = d3.scaleLinear()
    // .domain([1, d3.max(data, d => d.Value)])
    .domain([1, 1000])
    .range([0, width]); 
    

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
        .attr("r", d => xLinearScale(d.Value/20))
        .attr("fill", "pink")
        .attr("opacity", ".5")

   

});



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
var arr1=[];

function init(){
    var selector1 = d3.select("#places-menu");
    var selector2 = d3.select("#spieces-menu");
    var selector3 = d3.select("#condition-menu");
 
    data.forEach(row => {
        selector1
            .append('a')
            .attr("class","dropdown-item")
            .text(row.place);
    
    selector2
            .append('a')
            .attr("class","dropdown-item")
            .text(row.spieces);
    
    selector3
            .append('a')
            .attr("class","dropdown-item")
            .text(row.condition)
            arr1.push(row.place);
    });
    // alert(arr1);
}

init();

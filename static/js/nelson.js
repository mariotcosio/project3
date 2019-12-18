function buildPlot() {
    /* data route */
    /*url = "/api/test";
    d3.json(url).then(function(data){
      data.forEach(d => {
        console.log(d[0]);
      });
      //console.log(data);
    });*/
    
    var url = "/api/test";
    var svgWidth = window.innerWidth/1.4;
    var svgHeight = window.innerHeight;

    var margin = {
        top: 20,
        right: 40,
        bottom: 80,
        left: 100
    };

    var width = svgWidth - margin.left - margin.right;
    var height = svgHeight - margin.top - margin.bottom;

    // if the SVG area isn't empty when the browser loads,
    // remove it and replace it with a resized version of the chart
    var svgArea = d3.select("body").select("svg");

    // clear svg is not empty
    if (!svgArea.empty()) {
        svgArea.remove();
    }
    var svg = d3
        .select(".chart")
        .append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight);

        var chartGroup = svg.append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);
    
    // import data
    d3.json(url).then(function(data){
        var IUCN=[];
        var value =[];
        var spec=[];

        data.forEach(function(d){
            // console.log(d[0]);
            d[3]= +d[3];
            value.push(d[3]);
            IUCN.push(d[2]);
            spec.push(d[1]);
        });
    
        var xLinearScale = d3.scaleLinear()
        // .domain([1, d3.max(data, d => d.Value)])
        .domain([1, 500])
        .range([5, width]); 
        

        var yBandScale = d3.scaleBand()
            .domain(IUCN)
            .range([0, height]);

            var xAxis = d3.axisBottom(xLinearScale);
            var yAxis = d3.axisLeft(yBandScale);
            
        chartGroup.append("g")
                .attr("transform", `translate(0, ${height})`)
                .call(xAxis);
                
        chartGroup.append("g")
                .call(yAxis);

        var circlesGroup = chartGroup.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", d => xLinearScale(d[3]))
            .attr("cy", d => yBandScale(d[2]))
            .attr("r", d => xLinearScale(d[3]/30))
            .attr("opacity", ".8")
            .attr("stroke-width", "0.5")
            .attr("stroke", "white")
            .style("fill", function(d){
                    if(d[1] == "MAMMAL"){
                        return "purple";
                    }
                    else if(d[1]=="BIRD"){
                        return "violet";
                    }
                    else if(d[1]=="REPTILE"){
                        return "pink";
                    }    
                    else if(d[1]=="AMPHIBIAN"){
                        return "black";
                    }    
                    else if(d[1]=="VASCULAR_PLANT"){
                        return "red";
                    }   
                    else if(d[1]=="FISH_TOT"){
                        return "gray";
                    }
    
                    else
                    {
                        return "pink";
                    }
            });

        

        // circlesGroup
        // .on("mouseover", function(d){
        //         d3.select(this)
        //         .transition()
        //         .duration(1000)
        //         .attr("r",d => xLinearScale(d[3]/10))
        //         .style('opacity', 0.9)
        // })

        // .on("mouseout", function(){
        //         d3.select(this)
        //             .transition()
        //             .duration(1000)
        //             .attr("r", d => xLinearScale(d[3]/30))
        //             toolTip.style("display", "none");
        // });

     
        var div = d3.select("body").append("div") 
        .attr("class", "tooltip")       
        .style("opacity", 1);
        
        // var toolTip = d3.select("body")
        // .append("div")
        // .attr("class", "tooltip");


        circlesGroup.on("mouseover", function(data, i){
            d3.select(this)
            .transition()
            .duration(1000)
            .attr("r",d => xLinearScale(d[3]/10))
            .style('opacity', 0.9);

            div.transition()        
            .duration(200)      
            .style("opacity", 0.9);  

            // div.html(`${d[0]}<hr>${d[1]}<hr>${d[2]}`) 
            div.html(`${data[0]} <hr> ${data[1]} <hr> ${data[2]} <hr>${data[3]} <hr>`)
            .style("left", (d3.event.pageX) + "px")     
            .style("top", (d3.event.pageY - 28) + "px");
        })
        .on("mouseout", function(){
            d3.select(this)
                .transition()
                .duration(1000)
                .attr("r", d => xLinearScale(d[3]/30));

                div.transition()        
                .duration(500)      
                .style("opacity", 0);   
    });

    
    }).catch(function(error) {
            console.log(error);
        });  
};


buildPlot();
d3.select(window).on("resize", buildPlot);


 
// var url="/api/vulnerable";

function drawPlots(url, chartTitle){
    d3.json(url).then(function(data){
        console.log(data);
        var icun=[];
        var value=[];
        var spec=[];
        var cou=[];
        
        data.forEach(function(d){
            d.value= +d.value;
            value.push(d.value);
            icun.push(d.icun);
            spec.push(d.spec);
            cou.push(d.cou);
        });


    var trace1 = {
        x: cou,
        y: value,
        z: spec,
        type: "bar",
        mode: "marker",
        text: spec
        
    }; 

    
    var layout = {
        title: chartTitle,
        
        yaxis: {
        range: [1,200],
        type: "linear"
        },
        showlegend: false
    };

    
    var data1 = [trace1];            
    Plotly.newPlot("chart", data1, layout);
    });
}
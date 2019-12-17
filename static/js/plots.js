// var url="/api/vulnerable";

function drawPlots(url, chartTitle, chartType, barWidth){
    // alert(chartType);
    // alert(chartRange);

    d3.json(url).then(function(data){
      
        // console.log(data);
        // var icun=[];
        // var value=[];
        // var spec=[];
        // var cou=[];

        var mammal_value=[];
        var mammal_cou=[];

        var reptile_value=[];
        var reptile_cou=[];

        var bird_value=[];
        var bird_cou=[];


        data.forEach(function(d){
            d.value= +d.value;
            // value.push(d.value);
            // icun.push(d.icun);
            // spec.push(d.spec);
            // cou.push(d.cou);
            
            if (d.spec=="MAMMAL"){
                mammal_value.push(d.value);
                mammal_cou.push(d.cou);

            } else if (d.spec=="REPTILE") {
                reptile_value.push(d.value);
                reptile_cou.push(d.cou);

            } else  {
                bird_value.push(d.value);
                bird_cou.push(d.cou);

            }
        });


        console.log(mammal_value);
        console.log(mammal_cou);
        
        // console.log(bird);
        // console.log(reptile);
    

    var trace1 = {
        x: mammal_cou,
        y: mammal_value,
        name: "Mammals",
        type: "bar",
        marker: {
            color: 'rgb(49,130,189)',
            opacity: 0.7,
          },
        width: barWidth
    }; 
    var trace2 ={
        x: reptile_cou,
        y: reptile_value,
        name: "Reptiles",
        type: "bar",
        marker: {
            color: 'red',
            opacity: 0.5
        },
        width: barWidth
    }
    var trace3 ={
        x: bird_cou,
        y: bird_value,
        name: "Birds",
        type: "bar",
        marker: {
            color: 'rgb(142,124,195)',
            // opacity: 0.5
        },
        width: barWidth
    }
    


    var layout = {
        title: chartTitle,
        barmode: chartType,
        showlegend: true
    };

    
    var data1 = [trace1, trace2, trace3];            
    Plotly.newPlot("chart", data1, layout);
    });
}


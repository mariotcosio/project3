function buildPlot() {
    /* data route */
  var url = "/api/test";
  d3.json(url).then(function(response) {
    console.log("Why doe");
    console.log(response);

    /*var data = response;

    var layout = {
      title: "Pet Pals",
      showlegend: false,
      height: 600,
      width: 980
    };
    Plotly.newPlot("plot", data, layout);
  });*/
  });
};

buildPlot();

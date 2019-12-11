
 <div id="mapcontainer" align="center"> <!-- You can place the container wherever you want, but it has to be before loading the code-->
 <link rel="stylesheet" href="css/worldmap.v1.css"> 
 <script src="js/worldmap.v1.js"></script>
 <script>
 
 
    var createmap = new Worldmap({  
     elementid: "#mapcontainer",
      mapstyle: {   // Change the map style
             ocean: "#ffffff",
         region: "pink",
         border : "transparent"
     },
     project: {  
         name: "Aitoff",
         //zoomlevel: 6 // If you want it to zoom into an area
         //zoomarea:[-122.417, 37.775] 
                            },
     showtable:false, // Hide Table
     editpanel:false,  // Hide Edit
    data: // This is the format for the bubble data. Name (optional), coordinates, size (optional), and color(optional).
            [{name: 'Bubble 1', coordinates: [21.32,  -7.32], size: 45, color: 'red'},
  {name: 'Bubble 2', coordinates: [12.32, 27.32], size: 5, color: 'blue'},
  {name: 'Bubble 3', coordinates: [0.32, 23.32], size: 6, color: 'magenta'},
  {name: 'Bubble 3', coordinates: [-97,38], size: 35, color: 'darkblue'},
  {name: 'Bubble 3', coordinates: [-102,39], size: 40, color: 'magenta'},
  {name: 'Bubble 3', coordinates: [-80,40], size: 10, color: 'green'},
  {name: 'Bubble 3', coordinates: [-97,29], size: 10, color: 'black'},
  {name: 'Bubble 3', coordinates: [-70,38], size: 37, color: 'red'},
  {name: 'Bubble 3', coordinates: [-89,47], size: 20, color: 'blue'},
  {name: 'Bubble 3', coordinates: [-110,36], size: 17, color: 'white'},
  {name: 'Bubble 3', coordinates: [-130,36], size: 37, color: 'white'},
  {name: 'Bubble 3', coordinates: [-150,86], size: 17, color: 'red'},
  {name: 'Bubble 3', coordinates: [-110,16], size: 27, color: 'blue'},
  {name: 'Bubble 3', coordinates: [-90,36], size: 10, color: 'black'},
  {name: 'Bubble 3', coordinates: [-60,38], size: 40, color: 'red'},
  {name: 'Bubble 3', coordinates: [-80,49], size: 27, color: 'blue'},
  {name: 'Bubble 3', coordinates: [-115,32], size: 7, color: 'white'},
  {name: 'Bubble 3', coordinates: [0.32, 23.32], size: 5, color: 'magenta'},
  {name: 'Bubble 4', coordinates: [-31.32, 23.32], size: 5, color: 'black'}],
  plugin: "bubbles", // specify the name of the plugin 
    defaultfill: "steelblue", // default fill color
    zoomable: false, // disable zooming
    defaultsize: 30,
    }); 
  
 setTimeout(function(){createmap.update([{"location":"MX","2008":"4487.21683","2009":"3613.37333","2010":"3117.170779"},{"location":"US","2008":"2014","2009":"4924","2010":"2345"},{"location":"CA","2008":"4079.154455","2009":"6582.25541","2010":"3377.846283"},{"location":"RU","2008":"13798.98219","2009":"10222.43894","2010":"14935.56198"},{"location":"BR","2008":"16823.42243","2009":"4667.990667","2010":"14900.90889"},{"location":"CO","2008":"2436.276018","2009":"19398.35665","2010":"18885.26967"},{"location":"GB","2008":"16823.42243","2009":"4667.990667","2010":"14900.90889"},{"location":"DZ","2008":"4079.154455","2009":"6582.25541","2010":"3377.846283"},{"location":"GL","2008":"16823.42243","2009":"4667.990667","2010":"14900.90889"},{"location":"NO","2008":"4079.154455","2009":"6582.25541","2010":"3377.846283"}],"barchart")}, 4000)
 
$( document ).ready(function() {

  var url = 'http://127.0.0.1:8000/books/charts/1';
  
  var processed_json = new Array();

  $.getJSON(url, function(data) {
    
    // Populate series
    for (i = 0; i < data.length; i++){
      processed_json.push([data[i].key, data[i].value]);
    };
 
    var title = {
        text: 'Books by Author'
      };

    var series = [{
        type: 'pie',
        name: 'books no.',
        data: processed_json
      }];

    var tooltip = {
        pointFormat: '<b>{point.y}</b>'
      };

    var plotOptions = {
      pie: {
        dataLabels: {
          enabled: true,
          format: '<b>{point.name}</b>: {point.percentage:.1f} %'
        },
        showInLegend: false
      }
    };

    var credits = {
      enabled: false
    };

    var json = {};

    json.title = title;
    json.series = series;
    json.tooltip = tooltip;
    json.plotOptions = plotOptions;
    json.credits = credits;

    $('#con1').highcharts(json);

  });

})
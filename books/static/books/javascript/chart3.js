$(document).ready(function() {

    var title = {
      text: 'Top 3 authors'
    };

    var xAxis = {
      categories: chart3_data['x'],
      title: {
        text: null
      }
    };

    yAxis = {
      min: 0,
      title: {
        text: null,
        align: 'high'
      },
      labels: {
        overflow: 'justify'
      }
    };

    var tooltip = {
      pointFormat: '{series.name}: <b>{point.y}</b>'
    };

    var plotOptions = {
      bar: {
        dataLabels: {
          enabled: true
        }
      }
    };

    var series = [{
      type: 'bar',
      name: 'book no.',
      data: chart3_data['y']
    }];

    var credits = {
        enabled: false
      };

    var json = {};

    json.title = title;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.tooltip = tooltip;
    json.plotOptions = plotOptions;
    json.series = series;
    json.credits = credits;
  
    $('#chart3').highcharts(json)
    
});


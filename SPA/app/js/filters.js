'use strict';

/* Filters */

var appFilters = angular.module('roomTaken.filters', []);

appFilters.filter('showToBeThisWeek', function() {
    return function(input) {
//        console.log(input);
//        var input = new Date(input);
//        console.log(input);
//        console.log(input.getDay());
//        var dateThisWeek = new Date();
//        console.log(dateThisWeek.setDay(input.getDay()));
//        dateThisWeek.setDay(input.getDay());
//        
//        return dateThisWeek;
  };
});

appFilters.filter('filterSeats', function() {
    return function(input, condition) {
        var results = [];
        
        if (!condition)
            return input;
        
        if (!isNumeric(condition))
            return input;
        
        for (var i in input) {
            if (isNumeric(i)) {
                var seats = input[i].seats;
                var percent = 10;
                var tolerance = (seats * percent) / 100;
                
                if (seats >= condition)
                    results.push(input[i]);
            }
        }
        
        results.sort(function(a,b)
                     {return b-a
                     });
        
        return results;
  };
});


function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}
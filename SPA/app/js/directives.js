'use strict';

/* Directives */

var appDirectives = angular.module('roomTaken.directives', []);

appDirectives.directive('searchKeyUp', function () {
    return {
        restrict: 'A',
        transclude: true,
        link: function (scope, elem, attrs) {
            console.log('dgasd');
        
            elem.bind("keypress", function (event) {
                if(event.keyCode === 13) {
                    scope.$apply(function (){
                        scope.$eval(attrs.searchKeyUp);
                    });

                    event.preventDefault();
                }
            });
        }
    }
});

'use strict';


// Declare app level module which depends on filters, and services
angular.module('roomTaken', [
  'ngRoute',
  'roomTaken.filters',
  'roomTaken.services',
  'roomTaken.directives',
  'roomTaken.controllers',
  'gettext',
  'restangular'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {templateUrl: 'partials/home.html', controller: 'HomeCtrl'});
  $routeProvider.when('/search', {templateUrl: 'partials/search.html', controller: 'MyCtrl2'});
  $routeProvider.otherwise({redirectTo: '/home'});
}]);


angular.module('roomTaken').constant('constants', {
    "serverAddress": "http://10.0.200.186:8000/"
});
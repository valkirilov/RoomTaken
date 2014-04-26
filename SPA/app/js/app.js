'use strict';


// Declare app level module which depends on filters, and services
angular.module('roomTaken', [
  'ngRoute',
  'ngCookies', 
  'ngAnimate',
  'roomTaken.filters',
  'roomTaken.services',
  'roomTaken.directives',
  'roomTaken.controllers',
  'gettext',
  'restangular',
  'fx.animations',
//'omnibox'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {templateUrl: 'partials/home.html', controller: 'HomeCtrl'});
  $routeProvider.when('/search', {templateUrl: 'partials/search.html', controller: 'MyCtrl2'});
  $routeProvider.otherwise({redirectTo: '/home'});
}]);

angular.module('roomTaken').config(function($httpProvider) {
    //Enable cross domain calls
      $httpProvider.defaults.useXDomain = true;

      //Remove the header used to identify ajax call  that would prevent CORS from working
      //delete $httpProvider.defaults.headers.common['X-Requested-With'];
});



angular.module('roomTaken').constant('constants', {
    "serverAddress": "http://10.0.11.20:8000/"
});
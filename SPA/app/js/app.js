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
  'ui.bootstrap',
  //'fx.animations'
]).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/home', {templateUrl: 'partials/home.html', controller: 'HomeCtrl'});
    $routeProvider.when('/search', {templateUrl: 'partials/search.html', controller: 'MyCtrl2'});
    $routeProvider.when('/login', {templateUrl: 'partials/login.html', controller: 'MyCtrl2'});
    $routeProvider.when('/logout', {templateUrl: 'partials/logout.html', controller: 'LogoutCtrl'});
    $routeProvider.otherwise({redirectTo: '/search'});
}]);

angular.module('roomTaken').config(function($httpProvider) {
    //Enable cross domain calls
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $httpProvider.defaults.useXDomain = true;
    //$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{% csrf_value %}'

      //Remove the header used to identify ajax call  that would prevent CORS from working
      //delete $httpProvider.defaults.headers.common['X-Requested-With'];
});



angular.module('roomTaken').constant('constants', {
    "serverAddress": "http://localhost:8000/",
    "loginSuccess": "You are logged now ^_^",
    "loginFail": "Login failed :(",
    "registerSuccess": "Registration completed",
    "registerFail": "Registration Failed :(",
    "logout": "Come back again :(",
    "saveSuccessful": "Your draft is saved :)",
    "sendSuccessful": "Your card will be send :)"
});

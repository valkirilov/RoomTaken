'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('MyCtrl1', ['$scope', 'gettextCatalog', function($scope, gettextCatalog) {
      $scope.lang = "bg";
      
      $scope.setLanguage = function(language) {
          alert('Setting ' + language);
          gettextCatalog.currentLanguage = language;
      };
  }])
  .controller('MyCtrl2', [function() {

  }]);
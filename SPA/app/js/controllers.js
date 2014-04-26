'use strict';

/* Controllers */

angular.module('roomTaken.controllers', [])
.controller('GlobalCtrl', ['$rootScope', '$scope', 'LanguageService', function($rootScope, $scope, LanguageService) {
    $rootScope.languageService = LanguageService;
    
    
}])
.controller('HomeCtrl', ['$scope', function($scope) {

}])
.controller('MyCtrl2', ['$scope', 'ResourceService', function($scope, ResourceService) {
    
    $scope.snippets = null;
    
    $scope.schedule = null;
    
    $scope.init = function() {
        
        
        ResourceService.getSchedule().then(function(success) {
            $scope.schedule = success;
        }, function(error) {
            console.log(error);
        });
        
    };
    

    $scope.init();
}]);
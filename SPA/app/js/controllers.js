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
    
    $scope.init = function() {
        
        console.log(ResourceService);
        
        ResourceService.getSnippets().then(function(success) {
            console.log(success);
        }, function(error) {
            console.log(error);
        });
        
    };
    

    $scope.init();
}]);
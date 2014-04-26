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
    
    $scope.shedule = null;
    
    $scope.init = function() {
        
        console.log(ResourceService);
        
        ResourceService.getSnippets().then(function(success) {
            console.log(success);
        }, function(error) {
            console.log(error);
        });
        
        ResourceService.getShedule().then(function(success) {
            console.log(success);
            $scope.shedule = success.data.shedule;
        }, function(error) {
            console.log(error);
        });
        
    };
    
    function getTextStartWith(text, startChar){
        var toReturn = "";
        if(text.indexOf(startChar) > -1){
            var pos = text.indexOf(startChar);
            console.log(pos);
            while(text[pos] != ' ' && text[pos] != '\n' && pos < text.length -1){
                console.log(text[pos]);
                toReturn += text[++pos];
            }
        }
        return toReturn;
    }

    $scope.changeSearchInput = function() {
        var text = $scope.search.text;
        var room, teacher, subject;
        if(text.length > 1){
            console.log("searching...");
            //var room = new RegExp("\#(\S+)\s?",text);
            room = getTextStartWith(text, "@");
            subject = getTextStartWith(text, "#");

            console.log("ROOM " + room);
            console.log("SUBJECT " + subject);
            ResourceService.getSchedule(room, subject).then(function(success) {
                $scope.schedule = success.data;

            }, function(error) {
                conole.log("Error");
                console.log(error);
            });
        }        
    };



    $scope.init();
}]);
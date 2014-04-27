'use strict';

/* Controllers */

angular.module('roomTaken.controllers', [])
.controller('GlobalCtrl', ['$rootScope', '$scope', 'LanguageService', function($rootScope, $scope, LanguageService) {
    $rootScope.languageService = LanguageService;
    
    
}])
.controller('HomeCtrl', ['$scope', function($scope) {

}])
.controller('MyCtrl2', ['$scope', 'ResourceService', function($scope, ResourceService) {
    
    $scope.search = { text: "", type: "" };
    
    $scope.schedule = null;
    $scope.keywords = {};
    
    $scope.datepickers = {
        "isOpenedFromDate": false,
        "isOpenedToDate": false
    };
    
    $scope.minDate = new Date();
    $scope.fromDate = new Date();
    $scope.toDate = new Date();
    
    $scope.hstep = 1;
    $scope.mstep = 15;
    
    $scope.init = function() {
        
        
        ResourceService.getSchedule().then(function(success) {
            $scope.schedule = success;
        }, function(error) {
            console.log(error);
        });
        
        
//        ResourceService.getFreeRooms().then(function(success) {
//            //$scope.schedule = success;
//        }, function(error) {
//            console.log(error);
//        });
        
    };
    
    $scope.openDatepicker = function($event, datepickerOption) {
        
        $event.preventDefault();
        $event.stopPropagation();
        console.log($scope.datepickers);
        console.log(datepickerOption);
        $scope.datepickers[datepickerOption] = true;
        console.log($scope.datepickers);
    };
    
    $scope.removeKeyord = function(keyword) {
        delete $scope.keywords[keyword.type];
        $scope.makeSearch();
    };
    
    function getTextStartWith(text, startChar){
        var toReturn = "";
        if(text.indexOf(startChar) > -1){
            var pos = text.indexOf(startChar)+1;
            //console.log(pos);
            while(text[pos] !== ' ' && (pos < text.length)){
                //console.log(pos + ": " + text[pos]);
                toReturn += text[pos];
                pos++;
            }
        }
        return toReturn;
    }

    $scope.changeSearchInput = function() {
        var text = $scope.search.text;
        console.log($scope.search.text);
        var room, teacher, subject;
        if(text.length > 1){
            console.log("searching...");
            //var room = new RegExp("\#(\S+)\s?",text);
            room = getTextStartWith(text, "*");
            subject = getTextStartWith(text, "#");
            teacher = getTextStartWith(text, "@");
            
            if (room !== '')
                $scope.keywords['room'] = { type:'room', text: room };
            if (subject !== '')
                $scope.keywords['subject'] = { type:'subject', text: subject };
            if (teacher !== '')
                $scope.keywords['teacher'] = { type:'teacher', text: teacher };

            $scope.search.text = "";
            
        }
        $scope.makeSearch();
    };
    
    $scope.makeSearch = function() {
        var response;
        console.log($scope.search.free);
        if ($scope.search.free) {
            var keywords = {
                "from_date": $scope.fromDate,
                "to_date": $scope.toDate,
            };
            console.log(keywords);
            response = ResourceService.getFreeRooms(keywords);
        }
        else {
            response = ResourceService.getSchedule($scope.keywords);
        }
        
        response.then(function(success) {
            console.log('Success');
            console.log(success);
            $scope.schedule = success;

        }, function(error) {
            console.log("Error");
            console.log(error);
//                $scope.schedule = null;
        });
    };
    


    

    $scope.init();
}]);
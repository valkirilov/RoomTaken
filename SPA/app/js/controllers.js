'use strict';

/* Controllers */

angular.module('roomTaken.controllers', [])
.controller('GlobalCtrl', ['$rootScope', '$scope', 'LanguageService', '$location', '$timeout', 'AuthService', '$cookieStore', 'constants',
                           function($rootScope, $scope, LanguageService, $location, $timeout, AuthService, $cookieStore, constants) {
    $rootScope.languageService = LanguageService;
    
    $rootScope.message = { text: "", visible: false, type: 'schedule' };
        
    $rootScope.$on('$viewContentLoaded', function(){
        //console.log('*** *** *** *** *** *** *** *** *** *** *** ***');
        //console.log('View is changed to ' + $location.path());
        
        AuthService.user = $cookieStore.get('user') || { isLogged: false };
        $rootScope.user = AuthService.user;            

        if ($location.path() === '/login' && $rootScope.user.isLogged) {
            $location.path('dashboard');
        }
        else if ($location.path() === '/dashboard' && !$rootScope.user.isLogged) {            
            $location.path('login');
        }
        else if ($location.path() === '/logout') {
            // Logout and redirect to home
            AuthService.logout();
            $rootScope.user.isLogged = false;

            //$rootScope.handleMessage(constants.logout);
            $timeout(function() {
                $location.path('/home');
            }, 1500);
        }
    });
                               
    $rootScope.logout = function() {
        AuthService.logout();
        $rootScope.handleMessage('Излязохте успешно :(');
        $timeout(function() {
            $location.path('index')
        }, 1000);
    };
                               
   $rootScope.handleMessage = function(info) {
        $rootScope.message.text = info;
        $rootScope.message.visible = true;

        $rootScope.hideMessage();
    };

    $rootScope.handleSuccess = function(success) {
        $rootScope.message.text = success;
        $rootScope.message.visible = true;
        $rootScope.message.type = 'success';

        $rootScope.hideMessage();
    };

    $rootScope.handleError = function(error) {
        
        $rootScope.message.text = error;
        $rootScope.message.visible = true;
        $rootScope.message.type = 'error';

        console.log($rootScope.message);
        $rootScope.hideMessage();
    };

    $rootScope.hideMessage = function() {
        $timeout(function() {
            $rootScope.message.visible = false;
            $rootScope.message.type = '';   
        }, 2100);

    };
}])
.controller('HomeCtrl', ['$scope', function($scope) {

}])
.controller('MyCtrl2', ['$rootScope', '$scope', 'ResourceService', 'AuthService', '$location', 'constants', 
                        function($rootScope, $scope, ResourceService, AuthService, $location, constants) {
    
    $rootScope.search = { text: "", type: "schedule" };
    
    $scope.schedule = null;
    $rootScope.keywords = {};
    
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
        
        /*
        ResourceService.getSchedule().then(function(success) {
            $scope.schedule = success;
        }, function(error) {
            console.log(error);
        });
        */
        
        
//        ResourceService.getFreeRooms().then(function(success) {
//            //$scope.schedule = success;
//        }, function(error) {
//            console.log(error);
//        });
        
    };
    
    $scope.login = function(username, password) {
        console.log('Login now');

        AuthService.login($scope.username, $scope.password).then(function(suceess) {
            console.log('Authorised and details are here');
            console.log(suceess);

            //AuthService.save(suceess[1], suceess[0].data.token);
            $rootScope.handleSuccess(constants.loginSuccess);
            $scope.successfullLogin();
        }, function(error) {
            console.log(error);
            //$scope.errorMessage = error.data;
            $rootScope.handleError(constants.loginFail);
       });
    };
    
    $scope.openDatepicker = function($event, datepickerOption) {
        
        $event.preventDefault();
        $event.stopPropagation();
        console.log($scope.datepickers);
        console.log(datepickerOption);
        $scope.datepickers[datepickerOption] = true;
        console.log($scope.datepickers);
    };
    
    $scope.successfullLogin = function() {
        $location.path('index');    
    };
    
    $rootScope.removeKeyord = function(keyword) {
        delete $rootScope.keywords[keyword.type];
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

    $rootScope.changeSearchInput = function() {
        var text = $rootScope.search.text;
        console.log($rootScope.search.text);
        var room, teacher, subject;
        if(text.length > 1){
            //console.log("searching...");
            //var room = new RegExp("\#(\S+)\s?",text);
            room = getTextStartWith(text, "*");
            subject = getTextStartWith(text, "#");
            teacher = getTextStartWith(text, "@");
            
            if (room !== '')
                $rootScope.keywords['room'] = { type:'room', text: room };
            if (subject !== '')
                $rootScope.keywords['subject'] = { type:'subject', text: subject };
            if (teacher !== '')
                $rootScope.keywords['teacher'] = { type:'teacher', text: teacher };

            $scope.search.text = "";
            
        }
        $scope.makeSearch();
    };
    
    $scope.makeSearch = function() {
        var response;
        console.log($rootScope.search.free);
        if ($rootScope.search.type === 'free') {
            var keywords = {
                "from_date": $scope.fromDate,
                "to_date": $scope.toDate,
            };
            console.log(keywords);
            response = ResourceService.getFreeRooms(keywords);
        }
        else if ($rootScope.search.type === 'schedule') {
            response = ResourceService.getSchedule($scope.keywords);
        }
        
        response.then(function(success) {
            console.log('Success');
            console.log(success);
            $scope.schedule = success;
            $rootScope.handleSuccess("Успешно търсене");

        }, function(error) {
            console.log("Error");
            console.log(error);
//                $scope.schedule = null;
            $rootScope.handleError("Няма резултати от вашето търсене.");
    
        });
    };
    
    $scope.reserveRoom = function(room) {
        console.log("Resrerve");
        console.log(room);
        
        var args = {
            "room": room, 
            "from_date": $scope.fromDate,
            "to_date": $scope.toDate
        };
        
        ResourceService.reserveRoom(args).then(function(success) {
            console.log(success);
            $scope.schedule = null;
            // add message for saved room
            $rootScope.handleSuccess("Стаята е резервирана успешно.");
        }, function(error) {
            console.log(error);
            $rootScope.handleError("Настъпи грешка при резервирането.");
        });
        
    };


    

    $scope.init();
}])
.controller('LogoutCtrl', ['$rootScope', '$scope', '$location', '$timeout', 'AuthService', 
                           function($rootScope, $scope, $location, $timeout, AuthService) {
    
    
                               
    //$scope.init();

}]);
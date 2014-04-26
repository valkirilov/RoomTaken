appServices.service('ResourceService', ['Restangular', '$http', 'constants',
function(Restangular, $http, constants) {
   
    Restangular.setBaseUrl(constants.serverAddress + 'api/');
    
    var getRoom = function() {
            
    };
    
    var getSchedule = function() {
        var promise = Restangular.allUrl('schedule/').getList();
        return promise;
    };
    
    this.getSchedule = getSchedule;
    
}]);
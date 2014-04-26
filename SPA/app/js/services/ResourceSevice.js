appServices.service('ResourceService', ['Restangular', '$http', 'constants',
function(Restangular, $http, constants) {
   
    Restangular.setBaseUrl(constants.serverAddress + 'api/');
    
    var getRoom = function() {
            
    };
    
    var getSchedule = function(room, subject) {
    
        var url = 'schedule/?';
        if(room){
            url += "room="+room+"&";
        }
        if(subject){
            url += "subject="+subject+"&";
        }
        
        var promise = Restangular.allUrl(url).getList();
        return promise;
    };
    
    this.getSchedule = getSchedule;
    
}]);
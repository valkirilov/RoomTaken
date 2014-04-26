appServices.service('ResourceService', ['Restangular', '$http', 'constants',
function(Restangular, $http, constants) {
   
    Restangular.setBaseUrl(constants.serverAddress + 'api/');
    
    var getRoom = function() {
            
    };
    
    var getSchedule = function(room, subject) {
        var url = 'js/data/shedule.json?';
        if(room){
            url += "room="+room+"&";
        }
        if(subject){
            url += "subject="+subject+"&";
        }

        var promise = $http.get(url);
        return promise;
    };
    
    this.getSnippets = getSnippets;
    this.getShedule = getShedule;
    
}]);
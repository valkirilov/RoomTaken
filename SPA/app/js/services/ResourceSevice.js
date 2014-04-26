appServices.service('ResourceService', ['Restangular', '$http', 'constants',
function(Restangular, $http, constants) {
   
    Restangular.setBaseUrl(constants.serverAddress + 'api/');
    
    var getRoom = function() {
            
    };
    
    var getSnippets = function() {
        
        $http.get(constants.serverAddress);
        
        //var promise = $http.get('js/data/snippets.json');
        var promise = $http.get(constants.serverAddress+'api/snippets/');
//        var promise = $http({method: "GET",
//                           url: constants.serverAddress+"api/snippets/?format=json",
//                             withCredentials: true,
//                           headers:{
//                'Access-Control-Allow-Origin': '*',
//                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
//                'Access-Control-Allow-Headers': 'Content-Type, X-Requested-With',
//                'X-Random-Shit':'123123123'
//            }});
        //var promise = Restangular.allUrl('snippets/').getList();
        return promise;
        
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
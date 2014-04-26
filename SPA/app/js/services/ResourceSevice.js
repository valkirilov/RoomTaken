appServices.service('ResourceService', ['Restangular', '$http', 'constants',
function(Restangular, $http, constants) {
   
    Restangular.setBaseUrl(constants.serverAddress + 'api/');
    
    var getRoom = function() {
            
    };
    
    var getSnippets = function() {
        
        //var promise = $http.get('js/data/snippets.json');
        var promise = $http.get(constants.serverAddress+'api/snippets/');
        //var promise = Restangular.allUrl('snippets/').getList();
        return promise;
        
    };
    
    this.getSnippets = getSnippets;
    
}]);
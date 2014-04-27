appServices.service('ResourceService', ['Restangular', '$http', 'constants', '$filter',
function(Restangular, $http, constants, $filter) {
   
    Restangular.setBaseUrl(constants.serverAddress + 'api/');
    
    var getRoom = function() {
            
    };
    
    var getSchedule = function(keywords) {
        var url = 'schedule/';
        console.log(keywords);
        var conditions = generateUrlWithParams(keywords);
        console.log(conditions);
        var promise = Restangular.allUrl(url+conditions).getList();
        return promise;
    };
    
    var getFreeRooms = function(keywords) {
        
        var url = 'free-rooms/';
        
        var dateNow = new Date();
        var dateAfter = new Date();
        var dateAfter = dateAfter.setHours(dateNow.getHours() + 1);
        
        console.log(keywords);
        
        keywords['from_date'] = keywords['from_date'] || dateNow;
        keywords['to_date'] = keywords['to_date'] || dateAfter;

        var dateFormat = 'yyyy-MM-d HH:mm:ss';
        keywords = {
            "from_date": {
                "text": $filter('date')(keywords['from_date'], dateFormat)
            },
            "to_date": {
                "text": $filter('date')(keywords['to_date'], dateFormat)
            }
        };
        
//        keywords = {
//            "from_date": {
//                "text": parseInt(keywords['from_date'].getTime() / 1000)
//            },
//            "to_date": {
//                "text": parseInt(keywords['to_date'].getTime() / 1000)
//            }
//        };
        
        
        console.log(keywords);
        var conditions = generateUrlWithParams(keywords);
        console.log(conditions);
        var promise = Restangular.allUrl(url+conditions).getList();
        return promise;
        
    };
    
    this.getSchedule = getSchedule;
    this.getFreeRooms = getFreeRooms;
    
    
    function generateUrlWithParams(params) {
        var url = "";   
        console.log(params);
        for (var param in params) {
            console.log(param);
            
            if (params[param].text === undefined ||
               params[param].text === "")
                continue;
            console.log(params[param].text);
            
            if (url === "")
                url = "?";
            else 
                url += "&";

            url += param + "=" + params[param].text;
        }

        return url;
    }
    
}]);

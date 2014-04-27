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
        
        
        //console.log(keywords);
        var conditions = generateUrlWithParams(keywords);
        console.log(conditions);
        var promise = Restangular.allUrl(url+conditions).getList();
        return promise;
        
    };
    
    var reserveRoom = function(input) {
        
        var url = 'free-rooms/';
        var promise = Restangular.allUrl(url);
        console.log(input);
        var args = filterDates(input);
        console.log(args);
        
        var newSchedule = {
            "room_id": input['room'].id,
            "from_date": args['from_date'].text,
            "to_date": args['to_date'].text
        };
        
        console.log(newSchedule);
        console.log(promise);
//        promise.then(function(success) {
//            console.log(success);
//            success.post(newSchedule);    
//        });
        return promise.post(newSchedule);    
        
        //return promise;
        
    };
    
    this.getSchedule = getSchedule;
    this.getFreeRooms = getFreeRooms;
    this.reserveRoom = reserveRoom;
    
    
    var filterDates = function(keywords) {
        var dateNow = new Date();
        var dateAfter = new Date();
        var dateAfter = dateAfter.setHours(dateNow.getHours() + 1);
        
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
        
        return keywords;
    };
    
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

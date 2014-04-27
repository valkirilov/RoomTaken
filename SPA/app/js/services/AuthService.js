appServices.service('AuthService', ['$http', '$cookieStore', 'Restangular', '$q', 'constants',
function($http, $cookieStore, Restangular, $q, constants) {
    
    var user = $cookieStore.get('user') || { isLogged: false };
    console.log("User is initialized from: " + (($cookieStore.get('user')) ? "cookie" : "false var"));
   
    setHeaders();
   
   var login = function(username, password) {           
       // Send a HTTP request to check is the user exist and to get it's token

       var promises = $q.all([
                checkCredentials(username, password),
                //getUserDetails(username)]);
       ]);
       
       return promises;
   };
    
    function checkCredentials(username, password) {
        // Send a HTTP request to check is the user exist and to get it's token
        var deferred = $q.defer();
        
        var promise = $http({
           method: 'POST',
           url: constants.serverAddress+'api/api-token-auth/',
           data: {
               username: username,
               password: password
           }
        }).then(function(success) { 
            deferred.resolve(success);
        }, function(error) {
            console.log('UserService.js: Error in checking user credentials.');
            deferred.reject(error);
        });

        return deferred.promise;
    }
    function getUserDetails(username) {
        console.log('Getting user details');
        var deferred = $q.defer();
       
        var conditions = generateUrlWithParams({ "username":username });
        var promise = Restangular.one('users/'+conditions).get().then(function(success) {
            deferred.resolve(success);
       }, function(error) {
           console.error('UserService.js: Error in getting user details.');
           deferred.reject(error);
       });
        
       return deferred.promise;
   };
   
   var logout = function() {
       // First clear the user values
       console.log('Logouting from service');
       user.username = null;
       user.token = null;
       user.isLogged = false;
       
       delete user.id;
       delete user.url;
       delete user.email;
       delete user.groups;
       
       console.log(user);
       
       // And the remove it from the cookies
       $cookieStore.put('user', user);
       //return user;
   }
   
   /* This is inner function which is used to store info about the user */
   var save = function(userDetails, token) {
       // Save them in the service
       console.log('Saving user with token' + token);
       user = userDetails[0];
       user.token = token;
       user.isLogged = true;
       
       console.log(user);
       
       // Set the headers for http request
       setHeaders();
       
       // Save a cookie with the data
       console.log(user);
       $cookieStore.put('user', user);
   };

   function setHeaders() {
       console.log('Setting default headers');
       if (user.isLogged) {
           $http.defaults.headers.common.Authorization = "Token " + user.token; 
           Restangular.setDefaultHeaders({Authorization: "Token " + user.token});
       }
   };

    var refreshUser = function() {
        user = $cookieStore.get('user') || { isLogged: false};
    }
    
   var getUser = function() {
       return user;
   };
   
   function generateUrlWithParams(params) {
        var url = "";   
        for (var param in params) {
            if (params[param] === undefined)
                continue;

            if (url === "")
                url = "?";
            else 
                url += "&";

            url += param + "=" + params[param];
        }

        return url;
    }
   var isLogged = function() {
       return user.isLogged;
   }
   
   this.user = user;
   this.login = login;
   this.logout = logout;
   this.save = save;
   
   // Public getters
   this.isLogged = isLogged;
   this.getUser = getUser;
   this.getUserDetails = getUserDetails;
   this.refreshUser = refreshUser;
}]);

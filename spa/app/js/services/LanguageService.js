angular.module('roomTaken.services', [])
.service('LanguageService', function(gettextCatalog) {
    
    var setLanguage = function(language) {
        alert('Set lang ' + language);
        gettextCatalog.currentLanguage = language;
    };
    
    
    this.setLanguage = setLanguage;
});
(function() {
    'use strict';

    var app = angular.module('fast-text', ['ui.router', 'ngSanitize'])

    app.config(['$stateProvider', '$urlRouterProvider', config]);

    app.filter('unsafe', function($sce) { return $sce.trustAsHtml; });

    function config($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise("/index");

        $stateProvider
            .state('fasttext', {
                url: "/index",
                template: "<fast-text></fast-text>"
            })
    }
}());

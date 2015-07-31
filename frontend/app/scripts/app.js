'use strict';

/**
 * @ngdoc overview
 * @name housingApp
 * @description
 * # housingApp
 *
 * Main module of the application.
 */
angular
  .module('housingApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    "firebase"
  ])
    .constant("FIREBASE_URL", "https://housingapp.firebaseio.com/")
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .otherwise({
        redirectTo: '/'
      });
  });

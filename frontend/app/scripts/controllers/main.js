'use strict';

/**
 * @ngdoc function
 * @name housingApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the housingApp
 */
angular.module('housingApp')
  .controller('MainCtrl', function ($scope, $log, FIREBASE_URL, $firebaseArray) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $scope.listings = $firebaseArray(new Firebase(FIREBASE_URL + "/listings"));
    $log.info($scope.listings);
    $log.info(FIREBASE_URL);
  });

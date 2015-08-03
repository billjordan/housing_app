'use strict';

/**
 * @ngdoc function
 * @name housingApp.controller:ListingCtrl
 * @description
 * # ListingCtrl
 * Controller of the housingApp
 */
angular.module('housingApp')
  .controller('ListingCtrl', function ($scope, $log, $routeParams, $firebaseObject, FIREBASE_URL) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $log.info($routeParams.listingIndex);
    $scope.apartment_listing = $firebaseObject(new Firebase(FIREBASE_URL + "/listings/" + $routeParams.listingIndex));
    $log.info($scope.apartment_listing);
  });

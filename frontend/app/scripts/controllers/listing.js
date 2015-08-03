'use strict';

/**
 * @ngdoc function
 * @name housingApp.controller:ListingCtrl
 * @description
 * # ListingCtrl
 * Controller of the housingApp
 */
angular.module('housingApp')
  .controller('ListingCtrl', function ($scope, $log, $routeParams, $firebaseArray, $firebaseObject, FIREBASE_URL) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $log.info($routeParams.listingIndex);
    
    //get listing for listingIndex from firebase db
    //$scope.apartmentListing = $firebaseObject(new Firebase(FIREBASE_URL + "/listings/" + $routeParams.listingIndex));
    var apartmentListings = $firebaseArray(new Firebase(FIREBASE_URL + "/listings/"));// + $routeParams.listingIndex));
    apartmentListings.$loaded().then(function(){
        $log.info(apartmentListings[1]);
        $scope.apartmentListing = apartmentListings[Number($routeParams.listingIndex)];
        $log.info($scope.apartment_listing);
        setPrevAndNextListing();
    })
        
    //set the index of next and previous listing for links
    function setPrevAndNextListing() {
        var prevListing = Number($routeParams.listingIndex) - 1;   
        var nextListing = Number($routeParams.listingIndex) + 1;   
        if(prevListing == 0) prevListing = apartmentListings.length - 1;
        if(nextListing == apartmentListings.length) nextListing = 0;
        $scope.prevListing = prevListing;
        $scope.nextListing = nextListing;
    }
});

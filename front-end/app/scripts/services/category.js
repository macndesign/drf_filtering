'use strict';

/**
 * @ngdoc service
 * @name appApp.category
 * @description
 * # category
 * Service in the appApp.
 */

function categoryService($http) {
  var apiUrl = 'http://localhost:8000';
  return {
    list: function (url) {
      return $http.get(url).then(function (response) {
          return response.data;
        }
      )
    },
    listTopLevel: function () {
      return $http.get(apiUrl + '/categories-top-level/').then(function (response) {
          return response.data;
        }
      )
    }
  }
}

angular
  .module('appApp')
  .service('categoryService', categoryService);

categoryService.$inject = ['$http'];

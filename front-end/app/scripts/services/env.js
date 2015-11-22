'use strict';

/**
 * @ngdoc service
 * @name appApp.env
 * @description
 * # env
 * Service in the appApp.
 */
angular.module('appApp')
  .service('envService', function () {
    return {
      apiHost: 'http://localhost:8000'
    }
  });

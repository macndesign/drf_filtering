'use strict';

/**
 * @ngdoc function
 * @name appApp.controller:CategoryCtrl
 * @description
 * # CategoryCtrl
 * Controller of the appApp
 */

function categoryCtrl(categoryService, envService) {
  var vm = this;
  vm.apiUrl = envService.apiUrl;

  vm.categories = function categories (url) {
    categoryService.list(url).then(
      function (response) {
        if (response.length) {
          vm.children = response;
        }
      }
    ).catch(
      function (response) {
        console.log(response);
      }
    );
  };

  function categoriesTopLevel () {
    categoryService.listTopLevel().then(
      function (response) {
        vm.categoriesTopLevel = response;
      }
    ).catch(
      function (response) {
        console.log(response);
      }
    );
  }

  categoriesTopLevel();
}

angular
  .module('appApp')
  .controller('CategoryCtrl', categoryCtrl);

categoryCtrl.$inject = ['categoryService', 'envService'];

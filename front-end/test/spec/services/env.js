'use strict';

describe('Service: env', function () {

  // load the service's module
  beforeEach(module('appApp'));

  // instantiate service
  var env;
  beforeEach(inject(function (_env_) {
    env = _env_;
  }));

  it('should do something', function () {
    expect(!!env).toBe(true);
  });

});

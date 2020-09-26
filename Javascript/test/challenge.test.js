const assert = require('assert');
const challenge = require('../src/index.js');

describe('Challenge tests', () => {

	describe('Exercise 1 Tests', function() {
		it('returns "hello" => "olleh"', function(done) {
			assert.equal(challenge.exercise_1("hello"), "olleh");
			done();
		});

		it('returns "ae" => "ea"', function(done) {
			assert.equal(challenge.exercise_1("ae"), "ea");
			done();
		});

		it('returns "a" => "a"', function(done) {
			assert.equal(challenge.exercise_1("a"), "a");
			done();
		});
	});

	describe('Exercise 3 Tests', function() {
		it('returns 0 => 0', function(done) {
			assert.equal(challenge.exercise_3(0), 0);
			done();
		});

		it('returns 1 => 1', function(done) {
			assert.equal(challenge.exercise_3(1), 1);
			done();
		});

		it('returns 2 => 4', function(done) {
			assert.equal(challenge.exercise_3(2), 4);
			done();
		});

		it('returns 3 => 9', function(done) {
			assert.equal(challenge.exercise_3(3), 9);
			done();
		});

		it('returns 4 => 16', function(done) {
			assert.equal(challenge.exercise_3(4), 16);
			done();
		});
	});

	describe('Exercise 4 Tests', function() {
		it('returns 0 => n*(n+1)/2', function(done) {
			n = 0
			assert.equal(challenge.exercise_4(0), ((n*(n+1))/2));
			done();
		});

		it('returns 5 => n*(n+1)/2', function(done) {
			n = 5
			assert.equal(challenge.exercise_4(5), ((n*(n+1))/2));
			done();
		});

	});

	describe('Exercise 5 Tests', function() {
		it('returns 0 => n*(n+1)/2', function(done) {
			n = 0
			assert.equal(challenge.exercise_5(0), ((n*(n+1))/2));
			done();
		});

		it('returns 5 => n*(n+1)/2', function(done) {
			n = 5
			assert.equal(challenge.exercise_5(5), ((n*(n+1))/2));
			done();
		});

	});

});
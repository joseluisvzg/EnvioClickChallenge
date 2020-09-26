const challenge = {};

challenge.exercise_1 = function(str){
	if(str.length > 1){
		let rev_str = [];
		for(let i=str.length; i >= 0 ; i--){
			rev_str.push(str[i]);
		}
		return rev_str.join('');
	}
	return str
}

challenge.exercise_3 = function(n){
	if(n > 0){
		return n*n;
	}
	return 0;
}

challenge.exercise_4 = function(n){
	if(n > 0){
		return n + challenge.exercise_4(n-1);
	}
	return 0;
}

challenge.exercise_5 = function(n){
	if(n > 0){
		let sum = 0;
		for(let i=1;i<=n;i++){
			sum += i;
		}
		return sum;
	}
	return 0;
}

module.exports = challenge;

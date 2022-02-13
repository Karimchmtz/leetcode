var buildArray = function(nums) {
    var array = [];
    for (i = 0; i < nums.length; i++){
        array.push(nums[nums[i]]);
    }
    return array;
};
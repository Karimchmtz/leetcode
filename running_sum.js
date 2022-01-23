var runningSum = function(nums) {
    var array = [];
    for (i = 0; i < nums.length; i++){
        var k = nums[i];
        if (i == 0)
        {
            array.push(k);
            continue;
        }
        else{
            k += array[i - 1];
            array.push(k);
            continue;
        }
    }
    return array;
};
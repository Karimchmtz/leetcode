var getConcatenation = function(nums) {
    const len = nums.length
    let i;
    for (i = 0; i < len; i++){
        nums.push(nums[i]);
    }
    return nums
};
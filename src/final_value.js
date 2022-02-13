var finalValueAfterOperations = function(operations) {
    var result = 0;
    for (index = 0; index < operations.length; index++){
        var str = operations[index];
        if (str[str.length - 1] == '+' || str[0] == '+' )
        {
            result++;
            continue;
        }
        else
        {
            result--;
            continue;
        }
    }
    return result;
};
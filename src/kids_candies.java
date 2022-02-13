import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Integer> kids = new ArrayList<>();
        for (int i = 0; i < candies.length; i++){
            kids.add(candies[i]);
        }
    
        List<Boolean> result = 
                kids.stream().map(i -> {
                    if (i + extraCandies >= Collections.max(kids)){
                        return true;
                    }
                    return false;
                }).collect(Collectors.toList());

        return result;
    }
}
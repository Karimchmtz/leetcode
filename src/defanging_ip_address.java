class Solution {
    
    public String defangIPaddr(String address) {

        String res = "";

        for (char c: address.toCharArray()){
            if (c != '.'){
                res  += c;
                continue;
            }
            else{
                res += "[.]";
                continue;
            }
        }

        return res;
    }
}
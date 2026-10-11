# Problem Name: 
#             1189. Maximum Number of Balloons


# Python Implementation


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq=Counter(text)

        return min(
            freq['a'],
            freq['b'],
            freq['l']//2,
            freq['o']//2,
            freq['n']
        )



# C++ Implementation

class Solution {
public:
    int maxNumberOfBalloons(string text) {
        
        unordered_map<char, int> freq;
        for (char ch: text){
            freq[ch]++;
        }
 

        return min({
                freq['a'],
                freq['b'],
                freq['l']/2,
                freq['o']/2,
                freq['n']
            });
    
}

};






# Go Implementation

func maxNumberOfBalloons(text string) int {
    freq := make(map[rune]int)

    for _,ch:=range text{
        freq[ch]++

    }

    return min(
            freq['a'],
            freq['b'],
            freq['l']/2,
            freq['o']/2,
            freq['n'],
        )
    
}
        
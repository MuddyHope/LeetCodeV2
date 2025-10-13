/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    my_dict = {}

    for (let i =0; i<nums.length; i++){
        if (my_dict.hasOwnProperty(target -nums[i])) {
            return [my_dict[target-nums[i]], i];
        }
        else {
            my_dict[nums[i]] = i
        }
    }
};
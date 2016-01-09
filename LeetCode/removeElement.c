#include <stdio.h>
int removeElement(int* nums, int numsSize, int val) {
	int i = 0;
	int slow=0,fast=0; 
	for(i=0; i < numsSize;i ++){
		if(nums[fast] == val){
			fast++;
		}else{
			nums[slow] = nums[fast];
			slow++;
			fast++;
		}
	}
	
	return slow;
}

int main(void) {
	// your code goes here
	int test[4] = {1,2,1,3};
	int test_val = 1;
	int ans =  removeElement(test,4,1);
	printf("%d ",ans);
}

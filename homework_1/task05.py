def maxsum_of_subarray(array, k):
    counter = 0
    predict_sum=0
    maxsum=0
    for i in range(len(array)):
        predict_sum+=array[i]
        if i >= k-1:
            maxsum = max(maxsum, predict_sum)
            predict_sum-=array[counter]
            counter+=1
    return maxsum

class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.counter, tweetId])
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        followers = self.followerMap[userId]
        followers.add(userId)
        res = []
        for each_follower in followers:
            if each_follower in self.tweetMap:
                index = len(self.tweetMap[each_follower]) - 1
                count, tweetId = self.tweetMap[each_follower][index]
                heapq.heappush(minHeap, [count, tweetId, each_follower, index - 1])
    
        print(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, each_followerId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[each_followerId][index]
                heapq.heappush(minHeap, [count, tweetId, each_followerId, index - 1])

        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
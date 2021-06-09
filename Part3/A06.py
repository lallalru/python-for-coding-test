import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = [] #우선순위 최소힙
    for i,v in enumerate(food_times):
        heapq.heappush(q, (v,i+1)) #(음식먹는데 필요한 시간, 음식번호)
    
    eat = 0 #음식먹는데 걸린 시간
    previous = 0 #직전에 다 먹은 음식 시간
    length = len(food_times) #남은 음식 개수
    
    while eat + ( (q[0][0]-previous) * length) <=k :
        now = heapq.heappop(q)[0] #최상위 힙의 음식먹는데 필요한 시간
        eat += ( (now-previous) * length)
        length -=1
        previous = now
    
    q.sort(key = lambda x : x[1]) #두번째 원소인 음식번호로 정렬
    #print(q, eat)
    
    return q[(k-eat)%length][1]


food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times,k))
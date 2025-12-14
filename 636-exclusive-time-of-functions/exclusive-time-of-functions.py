class Solution(object):
    def exclusiveTime(self, n, logs):
        stack=[]
        res=[0]*n
        prev_time=0
        for log in logs:
            fid,fun,time=log.split(':')
            fid,time=int(fid),int(time)

            if fun=='start':
                if stack:
                    res[stack[-1]]+=time-prev_time
                stack.append(fid)
                prev_time=time
            else:
                res[stack.pop()]+=time-prev_time+1
                prev_time=time+1
        return res
        
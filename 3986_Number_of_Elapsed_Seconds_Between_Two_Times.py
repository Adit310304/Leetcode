class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        arr_st = list(map(int, startTime.split(":")))
        arr_et = list(map(int, endTime.split(":")))
        st_second = 0
        et_second = 0

        for i in range(len(arr_st)):
            if i == 0:
                st_second += arr_st[i] * 60 * 60
                et_second += arr_et[i] * 60 * 60
            elif i == 1:
                st_second += arr_st[i] * 60
                et_second += arr_et[i] * 60
            else:
                st_second += arr_st[i]
                et_second += arr_et[i]

        return et_second - st_second 
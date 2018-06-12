"""
Camp1_Day2_assign1
"""


Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

x_sessions = Sessions_Attended['sessions']
data_sessions = x_sessions.split(',')

print ("I have attended " + str(len(data_sessions)) + " sessions!!")



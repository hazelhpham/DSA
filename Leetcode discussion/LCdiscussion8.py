# Q1: Similar to Collatz Conjecture (haven’t seen on LC before)
# somewhat close to sort integers by the power of two
# Starting from 1, generate a sequence - which denotes the operations used to reach the target
# 	* multiple by 2
# 	* floor division by 3

#i have done this;;
#this is sort integers by power values 

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPow(num):
            steps = 0
            while num != 1:
                if num %2 == 0:
                    num = num / 2
                    steps+=1
                elif num %2 != 0:
                    num = 3*num+1
                    steps+=1
            return steps
        power_vals = {}
        for num in range(lo,hi+1):
            power_vals[num] = getPow(num)
        power_vals = sorted(power_vals.items(), key = lambda x:x[1])
        return power_vals[k - 1][0]  
        #Return the number(not power)

# Example 1:
# # target = 1
# # output: ""
# # explanation: 1 (target) = 1, no operations needed

# Example 2:
# # target = 2 
# # output: "*"
# # explanation: 2 (target) = 1 * 2 

# Example 3:
# # target = 8 
# # output: "***"
# # explanation: 8 (target) = 1 * 2 * 2 * 2 

# Example 4:
# # target = 10 
# # output: "****/*"
# # explanation: 10 (target) = 1 * 2 * 2 * 2 * 2 // 3 * 2

# Example 5:
# # target = 3 
# # output: "****/*/"
# # explanation: 3 (target) = 1 * 2 * 2 * 2 * 2 // 3 * 2 // 3
# follow-up question - what if we call the method multiple times?
# code a solution for expanded scope
# follow-up question - code optimization for the expanded scope
# follow-up question - optimize it further


#Q2:
"""
The task of design interview was to create a program which would stream data from some eternal data provider to several applications that are running on a machine. 
External data provider sends info about trades being done on stock exchange. Other applications are run as separate processes on the same machine, they can ask your program to send them data about exchange data on certain stock. The main questions of the design were about how to transfer data from your process to other processes, how to support streaming of data of multiple stocks. There were also extra questions about what to do when other processes that queried data die, how do you manage the state of the application. There was no coding in my system design interview, 
we have just discussed different approaches to the problem and I drawed my solution on paper.
"""



#Q3:
"""


Design a mailbox which should do the two functions:


send a message.
retrieve all messages of a user.
After I finished the requirements, he asked me to extend the code to provide these two functions:


send an error message if a receiver doesn't exist.
send one message to multiple users.
The problem was very straighforward and easy. I was able to communicate my thoughts and ideas with the interviewer. But after I finished the interview, and I felt that I will proceed to the next stage, 
I realized that my code could be better and improved. I guess the time constraint of the interview, and the overall stress were playing against me.
For example: (1) create a new class to save users, and make it a singelton class which has a set to store the users. 
(2) have a methods which validates if a user exists or not.
"""
class MailBox:
    """
    Mailbox class to send messages and retrieve message history.
    """
    def __init__(self):
        self.user_manager = UserManager()  # Access the singleton user manager
        self.user_messages = {}  # Map user_id -> list of messages

    def send(self, message, user_ids):
        for user_id in user_ids:
            if not self.user_manager.validate_user(user_id):
                print(f"Error: User {user_id} does not exist.")
                continue

            if user_id not in self.user_messages:
                self.user_messages[user_id] = []
            self.user_messages[user_id].append(message)

    def message_history(self, user_id):
        if not self.user_manager.validate_user(user_id):
            print(f"Error: User {user_id} does not exist.")
            return []
        return self.user_messages.get(user_id, [])

    def save_user(self, user_id):
        self.user_manager.add_user(user_id)

"""
retrieve, save users with O(1) -> use both stack + dict
get message history from a specific user -> use userId to access O(1)
send one message to multiple users?
"""
def get_recent_messages(messages, start_index):
    """
    Returns a list of messages starting from the given index to the end of the list.
    """


chat_history = ["Hello!", "How are you?", "Let's meet up.", "See you soon!", "Take care!"]
print(get_recent_messages(chat_history, 2))  # ["Let's meet up.", "See you soon!", "Take care!"] expected

email_list = ["Meeting at 10 AM", "Project deadline", "Lunch tomorrow", "Status report"]
print(get_recent_messages(email_list, 1))  # ["Project deadline", "Lunch tomorrow", "Status report"] expected

notifications = ["New follower", "Comment on your post", "Like on your photo"]
print(get_recent_messages(notifications, 0))  # ["New follower", "Comment on your post", "Like on your photo"] expected

notifications = ["New follower", "Comment on your post", "Like on your photo"]
print(get_recent_messages(notifications, 7))  # [] expected


"""
To complete this exercise:
--------------------------
Implement the 'get_recent_messages' function. It should take a list of messages (messages) and a starting index (start_index), then return all messages from that index to the end of the list.

Exercise Breakdown:
-------------------
You can omit the 'stop' value in the slice notation:
 
my_list[index:]

It will include all elements from the 'start' index to the end of the list.
"""

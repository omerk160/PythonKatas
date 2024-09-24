app_healthy = True  # Global variable


def check_server_response(status_code):
    """
    Simulates checking a server response. If the status code is not 200,
    the application health is set to False.
    """
    global app_healthy



def reset_health_check():
    """
    Resets the application health to True, simulating a health recovery or manual reset.
    """
    global app_healthy


print(f"Initial app health: {app_healthy}")  # Expected: True

check_server_response(500)  # Simulate a bad response from the server
print(f"App health after bad response: {app_healthy}")  # Expected: False

reset_health_check()  # Reset the health manually
print(f"App health after reset: {app_healthy}")  # Expected: True

check_server_response(200)  # Simulate a good response from the server
print(f"App health after good response: {app_healthy}")  # Expected: True


"""
To complete this exercise:
--------------------------
- Implement the `check_server_response` function to set `app_healthy` to False if the status code isn't 200.
- Implement the `reset_health_check` function to manually reset the `app_healthy` status to True.

Exercise Breakdown:
-------------------
Use the `global` keyword to modify the `app_healthy` variable inside functions.

Example:

global_var = True

def change_global():
    global global_var
    global_var = False

"""

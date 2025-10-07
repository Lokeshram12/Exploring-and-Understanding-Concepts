import time

# Big dataset
users = [{"id": i, "name": f"User{i}"} for i in range(1_000_000)]
index = {user["id"]: user for user in users}

def find_user_linear(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


# Linear search
start = time.time()
find_user_linear(users, 999999)
print("Linear search:", time.time() - start, "seconds")

def find_user_index(index, user_id):
    return index.get(user_id, None)

# Indexed search
start = time.time()
find_user_index(index, 999999)
print("Indexed search:", time.time() - start, "seconds")

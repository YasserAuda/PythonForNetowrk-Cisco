def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))

# Call function with parameters assigned as above
profile_info("Yasser", 945)

# Call function with keyword arguments
profile_info(username="Mike", followers=342)

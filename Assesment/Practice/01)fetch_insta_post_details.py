# # import instaloader


# # d= instaloader.Instaloader()
# # name= input("Enter Your name :- ")

# # example=d.download_profile(name,profile_pic_only=False)

# #example 2

# import instaloader

# # Create an Instaloader instance
# L = instaloader.Instaloader()

# # Load a profile
# username=input("Enter Your UserName :-")
# profile = instaloader.Profile.from_username(L.context, username)

# # Get information about the profile
# print("Username:", profile.username)
# print("Followers:", profile.followers)
# print("Following:", profile.followees)

import instaloader

def get_instagram_profile_info(username):
    try:
        # Create an Instaloader instance
        L = instaloader.Instaloader()
        username=input("Enter your username : - ")
        # Retrieve the profile information for the specified username
        profile = instaloader.Profile.get_instagram_profile_info(L.context, username)
                

        # Display profile information
        print("Profile metadata:")
        print(f"- Username: {profile.username}")
        print(f"- Full name: {profile.full_name}")
        print(f"- ID: {profile.userid}")
        print(f"- Is private: {profile.is_private}")
        print(f"- Is business account: {profile.is_business_account}")
        print(f"- Is verified: {profile.is_verified}")
        print(f"- Biography: {profile.biography}")
        print(f"- Profile picture URL: {profile.profile_pic_url}")
        print(f"- Number of posts: {profile.mediacount}")
        print(f"- Number of followers: {profile.followers}")
        print(f"- Number of following: {profile.followees}")
        print(f"- External URL: {profile.external_url}")
        print(f"- IGTV videos: {profile.igtvcount}")
        print(f"- Saved media: {profile.saved_media_count}")
        print(f"- Business category: {profile.business_category_name}")

    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     # Replace 'example_user' with the Instagram username you want to fetch information about

#     username=input("Enter your username : - ")
    

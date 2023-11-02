import instaloader


d= instaloader.Instaloader()
name= input("Enter Your name :- ")

example=d.download_profile(name,profile_pic_only=True)
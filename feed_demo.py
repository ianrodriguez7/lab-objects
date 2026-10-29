"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet
 
 
def build_feed():
    keeper = User('soccer_keeper')
    captain = User('soccer_captain')
    coach = User('coach_c')
    users = [keeper, captain, coach]
 
    posts = [
        Tweet('coach_c', 'Fitness test at 7am tomorrow #Preseason'),
        Tweet('soccer_captain', 'Survived the beep test #Preseason'),
        Tweet('soccer_keeper', 'Clean sheet in the scrimmage today #CleanSheet'),
    ]
 
    captain.follow()
    captain.unfollow()
    coach.follow()
   
    posts[1].like()
    posts[1].unlike()
    posts[2].like()
 
    return users, posts
 
 
def main():
    users, posts = build_feed()
    for user in users:
        print(user)
    for post in posts:
        print(post)
        print(post.hashtags())
 
 
if __name__ == '__main__':
    main()
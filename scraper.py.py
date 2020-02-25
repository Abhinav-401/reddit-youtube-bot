import praw

reddit = praw.Reddit(client_id='Q9MUOqXsxdmnqw',
                     client_secret='NPL9Cm-onUwKxxtaUFfkunP5Kv0', password='PlanetSplitter2526',
                     user_agent='RedditBot', username='TesterBester_Binary')

subreddit = reddit.subreddit('python')

conversedict = {}
hot_python = subreddit.hot(limit=3)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}, subid: {}'.format(submission.title,
                                                                                                   submission.ups,
                                                                                                   submission.downs,
                                                                                                   submission.visited,
                                                                                                    submission.id))
        submission.comments.replace_more(limit=None)      #limit=0                                                                                        
        comments = submission.comments
        for comment in comments:
            print(20*'-')
            print(comment.body)
            if len(comment.replies) > 0:
                for reply in comment.replies:
                    print('REPLY:')
                    print("\t"+reply.body)                                                                                                    
'''
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if comment.id not in conversedict:
                conversedict[comment.id] = [comment.body,{}]
                if comment.parent() != submission.id:
                    parent = str(comment.parent())
                    conversedict[parent][1][comment.id] = [comment.ups, comment.body]
'''                    


# Dictionary Format#
'''
conversedict = {post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],

                post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],
                                            
                post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],
                }


'''
'''
for post_id in conversedict:
    message = conversedict[post_id][0]
    replies = conversedict[post_id][1]
    if len(replies) > 1:
        print('Original Message: {}'.format(message))
        print(35*'_')
        print('Replies:')
        for reply in replies:
            print(replies[reply])
'''            

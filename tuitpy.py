#!/usr/bin/env python
# encoding: utf-8


"""
A Python script for using Twitter from the command line.

Uses inspect and sys standard libraries.
Uses pygment and python-twitter open source libraries.

Usage: tuitpy.py flag [args]

    flag [args]:
      -dm user text 
        Send text as a DM to @user.
      -tl [count] 
        Show count tweets of your TL.
      -m [count] 
        Show count mentions.
      -t text 
        Tweet text.
      -gm [count] 
        Show count last DMs.
      -f [count [user]] 
        Show your last count favorites or user's
"""


import inspect
import sys

from pygments import console
import twitter


# INSERT YOUR TOKENS HERE:
# Twitter specific constants
_CONSUMER_KEY = ''
_CONSUMER_SECRET = ''
_ACCES_TOKEN_KEY = ''
_ACCES_TOKEN_SECRET = ''
_USERNAME = ''                  # don`t include the @, just your user name

# Local constants
_MAX_ARGS = 4

# Custom output format
console.codes['yellow_bg'] = '\x1b[43m'
    

def tweet(text=None):
    """
    Tweets the specified text from the authenticated user.
    
    Args:
        text    
            The text of the tweet.
    """

    if text is not None:
        text = str(text)
        text_length = len(text)
        if text_length > twitter.CHARACTER_LIMIT:
            print 'Your tweet is %d characters' % text_length
            return
        status = api.PostUpdate(text)
        print 'Tweet sent!'
        print format_tweet(status)
    else:
        print 'Usage: %s -t tweet' % sys.argv[0]
    
def send_message(user=None, text=None):
    """
    Sends text as a Direct Message to user.
    
    Args:
        user
            The ID or screen name of the recipient user.
        text
            The message text to be posted.
    """

    if user and text:
        user = str(user)
        text = str(text)
        text_length = len(text)
        if text_length > twitter.CHARACTER_LIMIT:
            print 'Your message is %d characters' % text_length
            return
        try:
            status = api.PostDirectMessage(user, text)
        except twitter.TwitterError:
            print 'Error! Message not sent!'
            print 'Are you sure that %s is a valid username or ID?' % user
        else:
            print 'Message sent!'
            print format_message(status)
    else:
        print 'Usage: %s -dm user text' % sys.argv[0]
    
def get_timeline(count=20):
    """
    Shows the last count tweets in your TL if it's specified. 
    The last 20 tweets if not.
    
    Args:
        count   
            Number of tweets to be displayed.
            Maximum 20.
    """

    try:
        count = int(count)
        timeline = api.GetFriendsTimeline(_USERNAME, count)
    except ValueError:
        print 'Usage: %s -tl [count]' % sys.argv[0]
    except twitter.TwitterError:
        print 'There is a problem with Twitter'
    else:
        timeline.reverse()
        print '\n\n'.join([format_tweet(tweet) for tweet in timeline])
    
def get_mentions(count=20):
    """
    Shows the last count mentions if it's specified. 
    The last 20 mentions if not.
    
    Args:
        count   
            Number of tweets to be displayed.
            Maximum 20.
    """

    mentions = api.GetMentions()
    try:
        count = int(count)
    except ValueError:
        print 'Usage: %s -m [count]' % sys.argv[0]
    else:
        mentions = mentions[:count]
        mentions.reverse()
        print '\n\n'.join([format_tweet(tweet) for tweet in mentions])   
    
def get_messages(count=20):
    """
    Shows the last count messages if it's specified. 
    The last 20 messages if not.

    Args:
        count   
            Number of messages to be displayed.
            Maximum 20.
    """

    direct_messages = api.GetDirectMessages()
    try:
        count = int(count)
    except ValueError:
        print 'Usage: %s -gm [count]' % sys.argv[0]
    else:
        direct_messages = direct_messages[:count]
        direct_messages.reverse()
        print '\n\n'.join([format_message(dm) for dm in direct_messages])

def favorites(count=20, user=None):
    """
    Shows the last count favorites for user if it's specified. 
    The last count favorites of authenticated user if not.
    
    Args:
        count   
            Number of tweets to be displayed.
            Maximum 20.
        user
            The ID or screen name of user whom favorites are fetched.
    """

    try:
        count = int(count)
        if user is None:
            favorites = api.GetFavorites()
        else:
            favorites = api.GetFavorites(str(user))
    except ValueError:
        print 'Usage: %s -f [count, [user]]' % sys.argv[0]
    except twitter.TwitterError:
        print 'There is a problem with Twitter'
    else:
        favorites = favorites[:count]
        favorites.reverse()
        print '\n\n'.join([format_tweet(tweet) for tweet in favorites])
    
def format_tweet(status):
    user = status.user
    name = console.colorize('red', '@%s' % user.GetScreenName())
    date = console.colorize('blue', '\t\t%s' % status.GetCreatedAt())
    text = console.colorize('black', '\t%s' % format_text(status.GetText()))
    return '\n'.join([name + date, text])
    
def format_message(status):
    sender = console.colorize('red', '@%s' % status.GetSenderScreenName())
    recipient = console.colorize('red', '@%s' % status.GetRecipientScreenName())
    date = console.colorize('blue', '\t\t%s' % status.GetCreatedAt())
    arrow = console.colorize('darkgray', ' -> ')
    text = console.colorize('black', '\t%s' % format_text(status.GetText()))
    return '\n'.join([sender + arrow + recipient + date, text])

def format_text(text):
    # Show mentions in a fancy way
    username = '@%s' % _USERNAME
    mention = console.colorize('darkgray', username)
    return text.replace(username, console.colorize('yellow_bg', mention))
    
def help():
    _flags =    [
                '-dm user text \n\tSend text as a DM to @user.',
                '-tl [count] \n\tShow count tweets of your TL.',
                '-m [count] \n\tShow count mentions.',
                '-t text \n\tTweet text.',
                '-gm [count] \n\tShow count last DMs.',
                '-f [count [user]] \n\tShow your last count favorites or user\'s'
                ]
    print 'Usage: %s flag [args]' % sys.argv[0]
    print
    print 'flag [args]:'
    print '\n'.join(['  ' + flag for flag in _flags])


# Dict with following format:
# flag: function
_ARGS = {
        '-help': help,
        '-dm': send_message,
        '-tl': get_timeline,
        '-m': get_mentions,
        '-t': tweet,
        '-gm': get_messages,
        '-f': favorites
        }


if __name__ == '__main__':
    api = twitter.Api(  _CONSUMER_KEY, _CONSUMER_SECRET,
                        _ACCES_TOKEN_KEY, _ACCES_TOKEN_SECRET)
    argc = len(sys.argv)
    if argc == 1 or argc > _MAX_ARGS or sys.argv[1] is '-help':
        help()
    else:
        try:            
            # Take arg number and default arg number in function
            function = _ARGS[sys.argv[1]]
            argspec = inspect.getargspec(function)
            args_num = len(argspec.args)
            default_args = 0
            if argspec.defaults is not None:
                default_args = len(argspec.defaults)
            
            def valid_arg_number(args_):
                same_arg_number = args_ == args_num
                mandatory_args = args_num - default_args
                not_few = same_arg_number or args_ >= mandatory_args 
                not_too_much = args_ <= args_num
                return not_few and not_too_much
            
            # Call the corresponding function
            function_args = argc - 2
            if function_args == 2 and valid_arg_number(2):
                function(sys.argv[2], sys.argv[3])
            elif function_args == 1 and valid_arg_number(1):
                function(sys.argv[2])
            elif function_args == 0 and valid_arg_number(0):
                function()
            else:
                help()
        except KeyError:
            help()
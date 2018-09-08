def Reply(ctx, msg):
    return "<@{}>, {}".format(ctx.message.author.id, msg)

def toembed(message, js = True):
    if js:
        return "`json\n{}\n```".format(message)
    else:
        return "```\n{}```\n".format(message)

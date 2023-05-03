class MessageUtils():
    def separate_name_from_message_with_post_cond(message, cond):
        words = message.split()
        index = words.index(cond)
        
        name = words[index-2]
        return name
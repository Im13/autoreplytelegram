# Step 1: Import Modules
import time, os, csv, configparser
from telethon import TelegramClient, events

# Step 2: Writing Auto reply code
def parse_api():
    # read the api id and hash from config file
    config_parser = configparser.ConfigParser()
    read_config = config_parser.read('api.ini')
    # if the file is not exists
    if not read_config:
        print("If you don't have api id and api, please get them from my.telegram.org")
        config_parser.add_section('API_CONFIG')
        api_id = input("Enter api id:")
        api_hash = input("Enter api hash:")
        # set to config
        config_parser.set("API_CONFIG", 'api_id', api_id.strip())
        config_parser.set("API_CONFIG", 'api_hash', api_hash.strip())

        # write to file
        with open('api.ini', 'w') as api: 
            config_parser.write(api)
    else:
        config_parser.read('api.ini')
        api_id = config_parser.get('API_CONFIG', 'api_id')
        api_hash = config_parser.get('API_CONFIG', 'api_hash')

    return api_id, api_hash

# parse the api
api_id, api_hash = parse_api()

# Step 3: Create the client object and establish the client connection
# use sequential_updates = True to respond to messages one at a time

client = TelegramClient('auto_reply', api_id, api_hash, sequential_updates=True).start()

# Messages of the auto reply
reply_msg = input("Enter your event:")

# Step 4: Define async main method
async def main():
    """
    # Step 5: define the event handler method and handle the incoming message
    # This python decorator will attach itself to the my_event_handler definition,
    # and basically means that on a NewMessage event, the callback function
    # you're about to define will be called:
    """
    @client.on(events.NewMessage(incoming=True))

    async def my_event_handler(event):
        # Check if thhe event is private 
        if event.is_private:
            # get the sender
            sender = await event.get_sender()
            user = sender.to_dict()
            msg = event.message.to_dict()
            msg_text = msg['message'].lower()
            count_filter = 0;

            print(msg_text)

            filter_word = ['xq', 'xien quay', 'xiên quay']

            for w in filter_word:
                if msg_text.find(w) >= 0:
                    count_filter = count_filter + 1
                    msg_text = msg_text.replace(w, "xiên ghepx2")

            if count_filter > 0:
                time.sleep(2)
                await event.reply(msg_text)

            # msg_text = msg['message'].split()

            # for word in msg_text:
            #     if word.startswith("ba"):
            #         word = word.replace('ba', 'ca')
            #         print(word)

            #         # auto reply to the message
            #         time.sleep(2)
            #         await event.reply(word)

            # save the log message to csv
            # file_exists = os.path.isfile('log.csv')
            # with open('log.csv', 'a+') as log_file:
            #     writer = csv.writer(log_file, lineterminator="\n")

            #     if not file_exists:
            #         writer.writerow(['user', 'message', 'Time'])
            #     else:
            #         writer.writerow("zxczxczx")

# The below code printing the start time
print(time.asctime(), '-', 'Auto-replying...')

# Step 6: The client run until disconnected
with client:
    # the client run intil completed
    client.loop.run_until_complete(main())
    # the client runs until disconnected
    client.run_until_disconnected()

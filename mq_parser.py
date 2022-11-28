import datetime

# Get in the function only if the file is directly initialized
if __name__ == "__main__":

    file_name = "rabbitHTML.txt"
    queue_messages = []

    # Open in read-only mode
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file.readlines():
            if '<pre class="msg-payload">' in line:  # Each record line starts with this str
                # Get only part of the line with the record
                formatted_line = line[31:-7]
                print(formatted_line[-4:])
                if formatted_line[-4:] == "\"}]}":
                    queue_messages.append(line[31:-7] + "\n")

    # Generate file name
    # [:-7] get substring without last 7 chars (remove milliseconds)
    # .replace() used to change forbidden file characters to legal ones
    mq_messages_file_name = "MQ_Messages_" + \
        str(datetime.datetime.now())[:-7].replace(" ", "_").replace(":", "-") + \
        ".txt"

    # Write mode ('w') makes file if not exists
    with open(mq_messages_file_name, "w", encoding="utf-8") as file:
        file.writelines(queue_messages)

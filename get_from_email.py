import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('james.lyons0@gmail.com', 'password')
mail.list()

mail.select('inbox')
typ, data = mail.search(None, 'ALL')
ids = data[0]
id_list = ids.split()
#get the most recent email id
latest_email_id = int( id_list[-1] )

#iterate through N messages in decending order starting with latest_email_id
#the '-1' dictates reverse looping order
for i in range( latest_email_id, latest_email_id-10, -1 ):
   typ, data = mail.fetch( i, '(RFC822)' )

   for response_part in data:
      if isinstance(response_part, tuple):
          msg = email.message_from_string(response_part[1])
          varSubject = msg['subject']
          varFrom = msg['from']

   if "HSE" not in varSubject: continue # we only want messages with 'HSE' in title

   f = open('messages/'+str(i)+'.txt','w');
   f.write(str(msg));  # write the message to a file
   f.close();
   print str(i)+'.txt' # show progress
   
mail.logout()   

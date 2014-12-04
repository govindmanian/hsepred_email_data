hsepred_email_data
==================

Get hsepred predictions of protein properties from server, then download everything from gmail, then parse into matlab

Each of the scripts here is meant to run separately.

The order to run things:

- sequence_list.txt # this is the list of ssequences we want HSE data for
- python hsepred_auto.py  # this sends the protein seqs to hsepred server, 1 every 10 minutes
- python get_from_email.py # hsepred sends emails, read the emails from gmail and write them to files
- matlab parse_email_messages.m # parse the text files output in previous step, output mat file of data
- matlab find_missing_seqs.m # if hsepred_auto.py fails for some reason, figure out which sequences still need to be run

---
title: Locate wallet file
source_url: https://github.com/monero-project/monero/issues/8265
author: arkadiy-telegin
assignees: []
labels: []
created_at: '2022-04-18T22:55:14+00:00'
updated_at: '2022-04-19T14:22:31+00:00'
type: issue
status: closed
closed_at: '2022-04-19T02:24:27+00:00'
---

# Original Description
Due to a terrible accident, I deleted my whole filesystem.

Luckily, I could restore a lot of files. Unluckily, there is no way to know the name of the restored files, only the type.

It seems that Monero GUI doesn't store any metadata in the wallet file, which makes it very difficult to find which of the hundreds of binary files of approx. 2kB is the monero wallet file.

So my question is, could I somehow make a script that would make monero-cli try to decrypt hundreds of files in hopes that one of them would be the sought wallet file?

I run Arch Linux.

Thanks!

# Discussion History
## selsta | 2022-04-18T22:56:40+00:00
the wallet files usually end with .keys, do the restored files have any extension?

## arkadiy-telegin | 2022-04-18T23:15:22+00:00
The restored file would be categorized as application/octet-stream. There's unfortunately no separate file type for keys.

## selsta | 2022-04-18T23:20:06+00:00
Ok, you have to rename the file you are testing to something with .keys in the name and then try

```
./monero-wallet-cli --wallet-file test.keys --password "your_password"
```

If it's not a proper keys file then monero-wallet-cli will close with exit code 1.

## hinto-janai | 2022-04-19T00:54:36+00:00
```
#!/bin/bash

folder="/your/path/here/"
log="/your/log/here/"
binary="/your/binary/here/"

printf "Password: "
read -s password 
echo "Working..."

for wallet in $(find $folder -size -5k) ;do
    "$binary" --wallet-file "$wallet" --password "$password" --command "wallet_info" >> "$log" &
done

sleep 1
grep "Filename" "$log"
```
this tests every file in `$folder` that is under 5kb and outputs it to a log file

replace `/your/path/here/` with whatever folder/path you want to search  
replace `/your/log/here/` with where you want to save the log  
replace  `/your/binary/here/` to the path of a monero-wallet-cli binary
and enter your password when the script starts

after it finishes, it'll show you every file that was a valid wallet

## selsta | 2022-04-19T02:24:27+00:00
@hinto-janaiyo thank you for a proper solution. Closing this here as the question seems answered.

## arkadiy-telegin | 2022-04-19T09:47:37+00:00
Thank you very much @selsta and @hinto-janaiyo. I am now going to try to recover it. 

## hinto-janai | 2022-04-19T14:22:30+00:00
@arkadiy-telegin

actually you might want to manually run `grep "Filename" "/your/log/here/"` afterwards 

`sleep 1` sometimes isn't enough time for monero-wallet-cli to finish writing to the log so the grep in the script doesn't work


# Action History
- Created by: arkadiy-telegin | 2022-04-18T22:55:14+00:00
- Closed at: 2022-04-19T02:24:27+00:00

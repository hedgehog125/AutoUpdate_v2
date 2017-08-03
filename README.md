Welcome to AutoUpdate v2 for Python!

To get started import "AutoUpdate.py"...

import AutoUpdate
Or from a directory:

import AutoUpdate/AutoUpdate

Next you must specify the database... e.g:

https://raw.githubusercontent.com/hedgehog125/AutoUpdateExample

If you want to run locally you can use file:///

So add to your code:

AutoUpdate.database = [Put your database here]

Then run init()...

AutoUpdate.init()
This will check for updates and download new versions.


Check Auto-Update/Test.py for an example.

If you want to make a database see: https://github.com/hedgehog125/AutoUpdate_v2_Database

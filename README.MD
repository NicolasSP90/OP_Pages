# Auto Download One Piece Chapters from MangaReader
The thing is. One Piece releases around 40 chapters a year.<br>
I've been reading it since 2005 (8 years after release in 1997) and every week I download the new released chapter.<br> 
<br>(in order to read them offline, if you want to know)<br><br>
Well, I decided to automate the process.<br>
The idea, is that the software will check the last downloaded chapter in the current folder and download the next one.<br>
Each chapter  will have its own folder, with the images inside of them.<br>
The website I will use is MangaReader.

For accessing the page, as a user, this is are the steps:
 - Go to the Manga Page
 - Select the chapter
 - Select Vertical or Horizontal (for this, it will be vertical)

But the thing is: ads will lock actions in the page. So basically the interaction, as a user, is the following:
 - Go to the Manga Page (with specified chapter)
 - Afew ads will pop is interacting with the page
 - Reject all cookies
 - Afew ads will pop is interacting with the page
 - Select Vertical / Horizontal
 - Afew ads will pop is interacting with the page
 - NOW the page can be interacter with

We also have an important step that is folder and file management:
 - The images must be saved in a specific folder
 - The images must be saved with a specific order (00, 01, 02...)
 - The images are usually .jpg, but can be other image types (.jpeg, png,)

I'm currently using PyCharm to work, and using OP_Pages_Main_Notebook.py as my testing and developing area.<br>
Once I'm satisfied with the results, I will transfer it to OP_Pages_Main without the notebook cells and create a executable file.

  ## TODO
- [ ] Create a module to get the current path (Replacing the "Path to (my) folder" Block
- [ ] Create a module to get Chapter folders (Replace the "chapter" variable in "Variables" Block
- [ ] Script without notebook cells
- [ ] Create .exe

# Future
Maybe in the future I will take this and create a more generic downloader.
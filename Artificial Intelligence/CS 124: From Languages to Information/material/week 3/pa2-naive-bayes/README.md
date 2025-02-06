# PA2 - Naive Bayes
## Recommended before Starting

We recommend checking out the following before getting started on PA2:

* The Week 2 videos and slides on Text Classification and Language Modeling.
* The Group Work 2 and slides on Naive Bayes and Sentiment Analysis
* Chapter 4 of Jurafsky and Martin (3rd ed.), particularly sections 4.1-4.5,
  4.7, 4.8
* Optionally the Pang, Lee, and Vaithyanathan (2002) paper on sentiment
classification

## Getting the Assignment

You can get started using the same steps you followed for PA1. To recap,
you'll want to:

1. Open a terminal (terminal for macOS and Linux, 
   Ubuntu for Windows for Windows, or SSH into Rice/Myth) the same way you 
   did for PA1. 

1. Clone the git repository for PA2 (this repository) into a folder of your 
   choice by typing this in your terminal:
      
        git clone https://github.com/cs124/pa2-naive-bayes.git

2. Enter the project root directory and activate your cs124 conda environment by
   doing:
   
        cd pa2-naive-bayes
        conda activate cs124
   
    You should now see `(cs124)` in front of your shell prompt. 

   You'll need to do this every time you open a new terminal and re-start your
   notebook server. You should have already created this conda environment 
   as part of PA0. If not, and you encounter an error, please go back and 
   follow the instructions there.

3. Start up your jupyter notebook server

        jupyter notebook

4. A window should open automatically in your default browser. If it didn't,
    the terminal output should contain a URL you can use to open the
    notebook in a browser of your choice.
   
5. From the Jupyter notebook file explorer window that opens, click on the
pa2.ipynb file to open and edit it.

### Google Colaboratory

1. Go to [colab.research.google.com](http://colab.research.google.com). 
   If prompted to open a notebook, hit cancel for now. You should double-check 
   that you are logged in to your Stanford Google account. If not, you can 
   switch accounts in the top right.
   
2. Now go to File->Open Notebook. Go to the GitHub tab. It will ask you to log 
   in to your GitHub account (if you don't have one it is easy to make one).
   Once you've done that, copy and paste the URL: 
   https://github.com/cs124/pa2-naive-bayes into the search box and hit enter. 
   It should show:
   
            Repository: cs124/pa2-naive-bayes
            Branch:  Main

   Click on pa2.ipynb below to load the notebook.
      

## [NOT RECOMMENDED] - Rice/Myth

Rice is the name of a group of machines made available for student use
by Stanford. Myth machines are similar, but specifically maintained by and
for the computer science department. For our purposes, they are interchangeable,
so you should feel free to use whichever one you prefer.

0. __[WINDOWS ONLY]__ If you are using Windows, you have two options. If you
were able to install Ubuntu for Windows according to the instructions above,
you can use that for your terminal/shell to SSH into Rice/Myth (although, if 
you were able to get Ubuntu for Windows set up we would strongly recommend that
you try to get things working locally instead of using Rice/Myth). If you
weren't able to install Ubuntu for Windows, you can instead download and install
PuTTY [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
to use as an SSH client. Install and run it. 

1. SSH into Rice/Myth.
   - __[macOS/Linux/Ubuntu for Windows]__

            ssh [Your SUNet]@rice.stanford.edu
            # OR
            ssh [Your SUNet]@myth.stanford.edu

   - __[Windows]__ Run PuTTY and when prompted, enter `rice.stanford.edu` or
    `myth.stanford.edu` in the box labeled Host Name. Do not change any of the
     other settings. Click open to open a connection, which will cause a 
     terminal window to pop up. You will then be prompted to log in.

    You'll be prompted for your Stanford SUNet account password. 
   You will also likely be asked to authenticate using 
   2-factor authentication.

2. Clone the git repository for PA2 in a location of your choice:
      
        git clone https://github.com/cs124/pa2-naive-bayes.git
   
3. Enter the project root directory and activate your cs124 conda environment 
   (you should have already created this as part of PA0. 
   If not, please go back and follow the instructions there): 
   
        cd pa2-naive-bayes
        conda activate cs124

4. Start up your jupyter notebook server without a browser.

        jupyter notebook --no-browser --port=[pick a number from 1025 to 65535]

5. You now need to set up port forwarding from Rice/Myth to your local machine:

   - __[macOS/Linux/Ubuntu for Windows]__ Open a new terminal window on your
    local machine (NOTE: don't close the one on Rice/Myth, that one needs to
     stay open) and enter the following command:

            ssh -NL [local port you'd like to use]:localhost:[port number you picked on rice/myth] [SUNet]@[rice/myth].stanford.edu

    If it worked correctly, nothing should happen and your terminal will appear 
    to hang. This is fine, you should keep it open to maintain the tunnel.

   - __[Windows]__ Go back to your PuTTY window. In the left-side navigation
    window and select Connection->SSH->Tunnels. In the right-hand side window,
     there will be a section labeled "Add new forwarded port". 
     
    Under Source port, type the local port you'd like to forward to. 
    Destination, type:

        [rice/myth].stanford.edu:[port your Jupyter notebook server is running on]
     
    Then, click "Add".

6. Finally, try opening a browser of your choice (i.e. Chrome, Firefox, Safari)
    and opening the URL:
    
        localhost:[local port number you chose]

    If everything worked correctly, you'll see the Jupyter file
    explorer. It may prompt you for an authentication token. If it does,
    go back to the terminal window that is running the Jupyter notebook server
    (on Rice/Myth). In the output, you should see some URLs with a portion that
    looks like "token=...". Copy the token from there and paste it into your
    browser where requested.
    
7. From the Jupyter notebook file explorer window that opens, click on the
pa2.ipynb file to open it. All your implementation will be done directly in the
   notebook.

# Submitting your Solution

## macOS/Linux

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. Upload the zip file as your solution to the PA2 Naive Bayes assignment in 
   Gradescope (http://www.gradescope.com).

3. If this doesn't work or the zip files seems to have issues, you can try
   submitting just the pa2.ipynb notebook and see if the autograder is 
   now able to run.  

## Ubuntu for Windows

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. To access the file easily from Windows (which you'll need to do if you
   want to upload it to Gradescope), you'll probably want to move or copy
   it to an easily accessible location in your Windows filesystem. The C
   drive in Windows is accessible in Ubuntu at `/mnt/c`, so you should copy
   it to some path there, like `/mnt/c/Users/[your Windows username]/Desktop`,
   which is the path to your Windows desktop directory.
   You can do this from your Ubuntu terminal by doing:
   
        cp /path/to/submission.zip /mnt/c/Users/[your Windows username]/Desktop

3. Upload the zip file as your solution to the PA2 Naive Bayes assignment in 
   Gradescope (http://www.gradescope.com).

## Google Colaboratory

1. Once you've saved all your changes, go to File->Download .ipynb to download
your notebook file to your local machine.
2. If your solution required any extra files, make sure they were located in
pa2-naive-bayes/deps. Go to the file explorer on the left-hand side and download
those as well.
3. Once you have pa2.ipynb and any deps files you need saved locally,
create a zip file (either from your OS's file explorer or the terminal), making
sure that it has the following structure:
   
        deps/
        pa2.ipynb

3. Upload the zip file as your solution to the PA2 Naive Bayes assignment in 
   Gradescope (http://www.gradescope.com).

## Rice/Myth

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. You will then need to download/copy the zip file from Rice/Myth to your
local machine.
   
   - __[macOS/Linux/Ubuntu for Windows]__
    
        Open a terminal on your local machine and run the following command to
        copy the submission zip file from Rice/Myth to your local machine.

            scp [SUNet ID]@[myth/rice].stanford.edu:/path/to/submission.zip /local/path/to/copy/to
    
        If you're using Ubuntu for Windows, we recommend choosing as your local
        path something starting with `/mnt/c`, as this is the UNIX path
        that corresponds to your Windows filesystem. This allows you to download
        the zip file to a location where it can be easily accessed directly
        from windows. For example, if you chose `/mnt/c/Users/[your Windows username]/Desktop`
        as your destination, the file will be saved to your Windows Desktop folder.

   - __[Windows]__ PSCP is another utility that should have been installed
    automatically when you installed PuTTY earlier. Find and run it. In the
     terminal window, you can run the command:
     
            pscp [Your SUNet]@rice.stanford.edu:/path/to/submission.zip c:\temp\submission.zip
    
    to download the file from Rice/Myth to your local machine. You should now
   be able to access the file locally at c:\temp\submission.zip
   
3. Upload the zip file as your solution to the PA2 Naive Bayes assignment in 
   Gradescope (http://www.gradescope.com).
